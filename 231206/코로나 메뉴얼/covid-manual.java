import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        char a=sc.next().charAt(0);
        int ac=sc.nextInt();
        char b=sc.next().charAt(0);
        int bc=sc.nextInt();
        char d=sc.next().charAt(0);
        int dc=sc.nextInt();
        if(((a=='Y' && ac>=37) && (b=='Y' && bc>=37)) || ((b=='Y' && bc>=37) && (d=='Y' && dc>=37)) || (a=='Y' && ac>=37) && (d=='Y' && dc>=37)){
            System.out.print('E');
        }
        else{
            System.out.print('N');
        }
    }
}