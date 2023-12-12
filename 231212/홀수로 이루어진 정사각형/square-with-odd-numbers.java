import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        for(int i=11;i<=11+(n-1)*2;i+=2){
            for(int j=0;j<=(n-1)*2;j+=2){
                System.out.print((i+j)+" ");
            }
            System.out.println();
        }
    }
}