import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt(), a=1, b=0 ,cnt=1;
        for(int i=0;i<n;i++){
            if(i%2==0){
                a=cnt;
                for(int j=0;j<n;j++){
                    System.out.print(a+" ");
                    a++;
                    cnt++;
                }
            }
            else{
                b=a+n-1;
                for(int j=0;j<n;j++){
                    System.out.print(b+" ");
                    b--;
                    cnt++;
                }
            }
            System.out.println();
        }
    }
}