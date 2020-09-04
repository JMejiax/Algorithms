// Time complexity at least O(n*(n-i)!) tal que i = i! > k
// n = string length
// Change the file name to 'Main'
/*
In this problem you have to find the permutations using the first N English capital letters. Since there can be many permutations, you have to print the first K permutations.

input:
Input starts with an integer T (≤ 100), denoting the number of test cases.
Each case contains two integers N, K (1 ≤ N ≤ 26, 1 ≤ K ≤ 30).

output:
For each case, print the case number in a line. Then print the first K permutations that contain the first N English capital letters in alphabetical order. If there are less than K permutations then print all of them.

*/
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;   

public class Main{

		static String cadena = "";
		static String abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
		static ArrayList<String> solution = new ArrayList<String>();
		
		static int[] memo = new int[100];
		public static int Factorial(int n){
			if(n == 1)
				return 1;
			if(memo[n] > 0)
				return memo[n];
			else
			 memo[n] = n*Factorial(n-1);
			return n*Factorial(n-1);
		}
		
		public static int Digitos(int k, int n){
			if(Factorial(n) > k)
			
				return n;
			return Digitos(k, n+1);
		}
		
		public static void Swap(int l, int r){
			char[] c = cadena.toCharArray(); 
			char temp = c[l]; 
			c[l] = c[r]; 
			c[r] = temp; 
			cadena = String.valueOf(c); 
		}		
		
		public static void Permutar(int l, int r){			
				if(l == r){
					solution.add(cadena);
				}else{
					for(int i = l; i<=r ; i++){
						Swap(l, i);
						Permutar(l+1, r);
						Swap(l, i);			
					}
				}
		}

		public static void main(String args[]){
      	int l = 0;
      	ArrayList<int[]> cases = new ArrayList<int[]>();
      	
      	Scanner in = new Scanner(System.in);
      	int t = in.nextInt();
      	
      	for(int i = 0; i<t; i++){
      		
      		int[] case1 = new int[2];
      		
      		int n = in.nextInt();
	      	int k = in.nextInt();
	      	
	      	case1[0] = n;
	      	case1[1] = k;
	      	
	      	cases.add(case1);
      	}
				
				for(int i = 0; i<t; i++){
      		System.out.println("Case " + (i+1) + ":");
      		
      		if(cases.get(i)[0] > 5){
      			l = Main.Digitos(cases.get(i)[1], 1);
      			Main.cadena = Main.abc.substring(cases.get(i)[0]-(l+1), cases.get(i)[0]);
      			Main.Permutar(0, Main.cadena.length()-1);
      			
      			Collections.sort(Main.solution);
      			for(int j = 0; j < cases.get(i)[1] ; j++){
      				if(Main.solution.size() > j)
      				System.out.println(Main.abc.substring(0, cases.get(i)[0]-(l+1)) + Main.solution.get(j)); 
      			}
      		
      		}else{
      			Main.cadena = Main.abc.substring(0, cases.get(i)[0]);
      			Main.Permutar(0, Main.cadena.length()-1);
      			Collections.sort(Main.solution);
      			for(int j = 0; j < cases.get(i)[1] ; j++){
      				if(Main.solution.size() > j)
      				System.out.println(Main.solution.get(j)); 
      			}
      		}  		
      		Main.solution.clear();
      	}      	
 	
		}
}




