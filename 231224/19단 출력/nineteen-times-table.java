public class Main {
    public static void main(String[] args) {
        for(int i=1;i<20;i++){
            for(int j=1;j<20;j++){
                if(j%2==0)
                System.out.println(i+" * "+j+" = "+(i*j));
                else
                System.out.print(i+" * "+j+" = "+(i*j));
                if(j%2!=0 && j<19)
                System.out.print(" / ");
            }
            System.out.println();
        }
    }
}