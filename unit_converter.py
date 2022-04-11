import pandas as pd
from sqlalchemy import create_engine
from collections import defaultdict
from typing import List
from exceptions import ConversionError, UnitNotFoundError


class UnitConverter:
    """A Utility class that converts units of measure of ingredient dosages into the desired unit of measure

        Example
        ---------------
        c = UnitConverter()
        ml_conversions = c.get_available_conversions('ml')
        litres = c.convert(5, 'ml', 'l')

        Attributes
        ---------------
        conversion_dict: Dictionary containing conversion factor data pulled from db file

        Methods
        ---------------
        __load_conversion_dict()
            Internal static method that transforms the data source into a nested dictionary for quick conversion factor
            lookups

        __can_convert(self, input_unit: str, output_unit: str)
            Internal method that checks if the input units are supported and if they're able to be converted into their
            output counterparts

        get_units(self)
            Returns list of all supported units

        get_available conversions(self, unit: str)
            Retrieves list of supported/convertible units based on the input unit

        convert(self, scalar: int, input_unit: str, output_unit: str)
            Converts the input scalar into its desired unit of measure
        """

    def __init__(self):
        self.__conversion_dict = self.__load_conversion_dict()

    @staticmethod
    def __load_conversion_dict():
        """
        Internal static method that transforms the data source into a nested dictionary for quick conversion factor
        lookups

        Returns:
        ---------------
        conversion_dict(dict[dict[str]]): Nested dictionary of units and conversion factors
        e.g {'g': {'kg': 0.001}, {'mg': 1000}, etc...}
        """

        engine = create_engine(r"sqlite:///db/units_of_measure.db")
        df = pd.read_sql('SELECT * FROM CONVERSION_FACTOR', engine)

        dd = defaultdict(list)
        for inp, out, ratio in zip(df['Unit_input'], df['Unit_output'], df['Conversion_ratio']):
            dd[inp].append({out: ratio})

        merged_dict = {}
        conversion_dict = {}
        for key, val in dd.items():
            for v in val:
                merged_dict.update(v)
            conversion_dict[key] = merged_dict
            merged_dict = {}

        return conversion_dict

    def __can_convert(self, input_unit: str, output_unit: str) -> bool:
        """
        Internal method that checks if the input units are supported and if they're able to be converted into their
        output counterparts

        Parameters:
        ---------------
        input_unit(str): input unit of measure
        output_unit(str): Output unit of measure

        Returns:
        ---------------
        boolean True, else -> raise Exception
        """

        if input_unit not in self.__conversion_dict:
            raise UnitNotFoundError(f"Unit '{input_unit}' not available for conversion")
        elif output_unit not in self.__conversion_dict[input_unit]:
            raise ConversionError(f"Unit '{output_unit}' not an available conversion for unit '{input_unit}'")
        else:
            return True

    def get_units(self):
        """
        Returns list of all supported units

        Returns:
        ---------------
        list[str]: Sorted list of all supported units
        """

        return sorted(list(self.__conversion_dict.keys()))

    def get_available_conversions(self, unit: str) -> List[str]:
        """
        Retrieves list of supported/convertible units based on the input unit

        Parameters:
        ---------------
        unit(str): unit of measure

        Returns:
        ---------------
        List[str]: Sorted list of supported/convertible units
        """

        unit = unit.lower()
        try:
            unit_list = list(self.__conversion_dict[unit.lower()].keys())
            return sorted(unit_list)

        except KeyError:
            raise UnitNotFoundError(f"Unit '{unit}' not available for conversion")

    def convert(self, scalar: int, input_unit: str, output_unit: str) -> int:
        """
        Converts the input scalar into its desired unit of measure

        Parameters:
        ---------------
        scalar(int): Scalar input
        input_unit(str): Unit of measure of input scalar
        output_unit(str): Unit of measure of output scalar

        Returns:
        ---------------
        output_scalar(int): Resulting scalar after conversion
        """

        input_unit = input_unit.lower()
        output_unit = output_unit.lower()

        if self.__can_convert(input_unit, output_unit):
            conversion_factor = self.__conversion_dict[input_unit][output_unit] if input_unit != output_unit else 1
            output_scalar = conversion_factor * scalar
            return output_scalar

