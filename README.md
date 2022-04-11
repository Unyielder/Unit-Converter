# Unit-Converter

A Utility class for units of measure conversions for scientific analysis.

## How to use
```python 
unit_converter = UnitConverter()
```

### Get list of all supported units
```python 
unit_converter.get_units()
```
`['g', 'g/l', 'g/ml', 'iu/g', 'iu/kg', 'iu/l', 'iu/mg', 'iu/ml', 'iu/ug', 'kg', 'kg/l', 'kg/ml', 'l', 'mg', 'ml', 'ng', 'nl', 'ug', 'ul']`

### Get available conversions for a specific unit

```python 
ml_conversions = unit_converter.get_available_conversions('ml')`
```
`['l', 'nl', 'ul']`

### Convert 5 mililitres into its desired unit of measure
```python 
litres = unit_converter.convert(5, 'ml', 'l')
```
 `0.005`