import java.applet.Applet;
import java.awt.Button;
import java.awt.Label;
import java.awt.TextArea;
import java.awt.TextField;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;




public class WeatherApplet extends Applet implements ActionListener {
   private TextField locationInput;
   private TextArea weatherInfoArea;
   private Button refreshButton;




   @Override
   public void init() {
       Label locationLabel = new Label("Enter Location:");
       add(locationLabel);




       locationInput = new TextField(20);
       add(locationInput);




       refreshButton = new Button("Refresh");
       refreshButton.addActionListener(this);
       add(refreshButton);




       weatherInfoArea = new TextArea(10, 30);
       add(weatherInfoArea);
   }




   @Override
   public void actionPerformed(ActionEvent e) {
       if (e.getSource() == refreshButton) {
           String location = locationInput.getText();
           String weatherData = getWeatherData(location);
           weatherInfoArea.setText(weatherData);
       }
   }




   private String getWeatherData(String location) {
       try {
           String apiUrl = "http://localhost:8080/WeatherServlet?location=" + location;
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
           return response.toString();
       } catch (Exception e) {
           return "Error fetching weather data: " + e.getMessage();
       }
   }
}
