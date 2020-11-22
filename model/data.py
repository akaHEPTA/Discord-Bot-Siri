class WeatherData:
    main: str
    description: str


class Weather:
    l: [WeatherData]


class Main:
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int


class Wind:
    speed: float


class Data:
    weather: Weather
    main: Main
    wind: Wind

