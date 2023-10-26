import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class PythonJavaIntegration{
    
public static void main(String[] args) throws IOException, InterruptedException {

    String path ="C:\\Users\\omert\\Task2\\DataTransfer.py" ;

    ProcessBuilder pb = new ProcessBuilder("python",path).inheritIO();
    Process process = pb.start();
    process.waitFor();
    BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
    String line="";
    while ((line = reader.readLine())!= null) {
        System.out.println(line);
    }
 

}


}