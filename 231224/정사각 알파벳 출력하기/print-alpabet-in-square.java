import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt(), a='A';
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                System.out.print((char)a);
                a++;
            }
            System.out.println();
        }
    }
}