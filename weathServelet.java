import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import org.json.JSONObject;




public class WeatherServlet extends HttpServlet {
   protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
       String location = request.getParameter("location");
       String weatherData = getWeatherData(location);
       response.setContentType("text/html");
       response.getWriter().write(weatherData);
   }




   private String getWeatherData(String location) {
       try {
           String apiKey = "sdhjwfw56783cbf238jb";
           String apiUrl = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + apiKey;




           URL url = new URL(apiUrl);
           HttpURLConnection conn = (HttpURLConnection) url.openConnection();
           conn.setRequestMethod("GET");




           BufferedReader reader = new BufferedReader(new InputStreamReader(conn.getInputStream()));
           StringBuilder response = new StringBuilder();
           String line;
           while ((line = reader.readLine()) != null) {
               response.append(line);
           }
           reader.close();




           JSONObject jsonResponse = new JSONObject(response.toString());
           JSONObject main = jsonResponse.getJSONObject("main");
           double temperature = main.getDouble("temp") - 273.15;
           double humidity = main.getDouble("humidity");
           JSONObject weather = jsonResponse.getJSONArray("weather").getJSONObject(0);
           String description = weather.getString("description");




           return "Location: " + location + "<br>"
                   + "Temperature: " + temperature + "°C<br>"
                   + "Humidity: " + humidity + "%<br>"
                   + "Description: " + description;
       } catch (Exception e) {
           return "Error fetching weather data: " + e.getMessage();
       }
   }
}


