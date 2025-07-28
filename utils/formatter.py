def format_weather(data):
    location = data['location']
    current = data['current']
    air_quality = current.get('air_quality', {})
   #forecast = data['forecast']['forecastday'][0]
    astro = data['forecast']['forecastday'][0]['astro']
    alerts = data.get('alerts', {}).get('alert', [])

    return {

        "location" : {

            "country" : location['country'],
            "localtime" : location['localtime'],
            "time_zone" : location['tz_id'],

        },
        "current": {

            "temp_c": current['temp_c'],
            "wind_dir": current['wind_dir'],
            "condition": current['condition']['text'],
            "wind_mph": current['wind_mph'],
            "wind_kph": current['wind_kph'],
            "precip_mm": current['precip_mm'],
            "precip_in": current['precip_in'],
            "humidity": current['humidity'],
            "feelslike_c": current['feelslike_c'],
            "feelslike_f": current['feelslike_f'],
            "heatindex_c": current['heatindex_c'],
            "heatindex_f": current['heatindex_f'],
            "dewpoint_c": current['dewpoint_c'],
            "dewpoint_f": current['dewpoint_f'],
            "vis_km": current['vis_km'],
            "vis_miles": current['vis_miles'],
            "uv_index": current['uv'],
            "vis_miles": current['vis_miles'],
        },
        "air_quality": {

            "pm2_5" : air_quality['pm2_5'],
            "pm10" : air_quality['pm10'],
            "us_epa_index" : air_quality['us-epa-index'] ,
            "CO": air_quality['co'],
            "no2": air_quality['no2'],
            "o3": air_quality['o3'],
            "so2": air_quality['so2']
        },
        "astro": {
            "sunrise" : astro['sunrise'],
            "sunset" : astro['sunset'],
            "moonrise" : astro['moonrise'],
            "moonset" : astro['moonset'],
            "moon_phase" : astro['moon_phase'],
        },
         "alerts": {
             "count": len(alerts),
            "items": alerts
         }           
            
    }
