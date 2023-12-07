import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int a,b,c;
        a=0;
        b=0;
        c=0;
        for(int i=1; i<n ;i++){
            if(i%12==0){
                c++;
            }
            else if(i%6==0){
                b++;
            }
            else if(i%3==0){
                b++;
            }
            else if(i%2==0){
                a++;
            }   
        }
        System.out.print(a+" "+b+" "+c);
    }
}