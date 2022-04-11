# Unit-Converter

A Utility class for units of measure conversions for scientific analysis.

## How to use
`unit_converter = UnitConverter()`

### Get list of all supported units
`unit_converter.get_units()`

returns: `['g', 'g/l', 'g/ml', 'iu/g', 'iu/kg', 'iu/l', 'iu/mg', 'iu/ml', 'iu/ug', 'kg', 'kg/l', 'kg/ml', 'l', 'mg', 'ml', 'ng', 'nl', 'ug', 'ul']`

### Get available conversions for a specific unit

`ml_conversions = unit_converter.get_available_conversions('ml')`

returns: `['l', 'nl', 'ul']`

### Convert 5 mililitres into its desired unit of measure
`litres = unit_converter.convert(5, 'ml', 'l')`

returns: `0.005`