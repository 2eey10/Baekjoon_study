import java.util.*;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();

        // Declare the array outside the loop
        int[] arr = new int[t];

        for (int i = 0; i < t; i++) {
            arr[i] = scan.nextInt();
        }

        int v = scan.nextInt();
        
        int cnt = 0;
        for (int i = 0; i < t; i++) {
            if (arr[i] == v) {
                cnt++;
            }
        } 

        System.out.print(cnt);
        
        scan.close();
    }
}
