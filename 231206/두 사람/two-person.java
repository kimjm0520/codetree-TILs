import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int aa = sc.nextInt();
        char am = sc.next().charAt(0);
        int ba = sc.nextInt();
        char bm = sc.next().charAt(0);
        if((aa>=19 && am=="M") || (ba>=19 && bm=="M")){
            System.out.print(1);
        }
        else{
            System.out.print(0);
        }

    }
}