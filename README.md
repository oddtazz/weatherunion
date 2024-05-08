# WeatherUnion

WeatherUnion is a sample project that utilizes data from [WeatherUnion](https://www.weatherunion.com) to retrieve weather information.

## Usage

To use this Python code, you need to follow these steps:

1. Register with [WeatherUnion](https://www.weatherunion.com) and obtain an API Key.
2. Modify the `config.json` file and add your API Key there.
3. Obtain the location ID from the PDF file (`locations.pdf`) from this [This repository](https://github.com/oddtazz/weatherunion/blob/main/locations.pdf). Select the appropriate localityId and add it to the `config.json` file.

## Getting Started

1. Clone this repository.
2. `pip install requests`
3. Modify the `config.json` file with your API Key and locality ID.
4. Run the Python script.

## Example Config.json

```json
{
 "location": "ZWL000000",
 "api_key": "your_api_key_here"
}
```

## Sample output
```~$ python weather.py
Temprature: 22.72 °C
Humidity: 83.32%
Wind Speed: 0.84 km/h
Wind Direction: 289.2 Degrees
Rain Intensity: 0.2 mm/min
Rain Accumulation: 6.8 mm/h
```

## Compatibility

This code has been tested with Python 3.12.3.
