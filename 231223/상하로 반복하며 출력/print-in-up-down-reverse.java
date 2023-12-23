import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt(), a=1, b=n;
        for(int i=0;i<n;i++){
            for(int j=1;j<=n;j++){
                if(j%2!=0){
                    System.out.print(a);
                }
                else{
                    System.out.print(b);
                }
            }
            System.out.println();
            a++;
            b--;    
        }
    }
}