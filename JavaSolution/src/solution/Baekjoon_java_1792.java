package solution;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;
/**
 * 1. a, b를 d로 나눈다(나머지는 버린다)
 * 2. 에라토스태네스 채와 뫼비우스 함수를 구한다.
 * 	
 * */
public class Baekjoon_java_1792 {
	static BufferedReader br;
	static StringTokenizer st;
	static int a, b, d;
	static boolean[] era;
	static ArrayList<Integer> pr;
	static int[] mu;
	static int[] musum;
	static int elements;
	public static void main(String[] args) throws NumberFormatException, IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine().trim());
		era = new boolean[230];
		pr  = new ArrayList<Integer>();
		mu = new int[50001];
		musum = new int[50001];
		findera(230);
		findmu(50001);
		
		
		for (int i = 0; i < N; i++) {
//			System.out.println("i: "+i);
			st = new StringTokenizer(br.readLine().trim());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			d = Integer.parseInt(st.nextToken());
			a=a/d;
			b=b/d;
			long elements=(long)a*b;
//			for (int j = 2; j <= a; j++) {
//				elements+=(long) mu[j]*(long)(a/j)*(long)(b/j);
//			}
//			System.out.println(elements);
			elements = computeSum(a,b);
			
//			}
//			System.out.println(elements);
		}
		System.out.println("complete");
	}
	private static void findmu(int number) {
		for (int i = 0; i < mu.length; i++) {
			mu[i]=1;
		}
		for (int i = 2; i < mu.length; i++) {
			int dividend = i;
			for (int j = 0; j < pr.size(); j++) {
				int divisor = pr.get(j);
				if(dividend%divisor==0) {
					dividend/=divisor;
					mu[i]*=-1;
				}
				if(dividend%divisor==0) {
					mu[i]*=0;
					break;
				}
			}
			if(dividend!=1) {
				mu[i]*=-1;
			}
			musum[i]=musum[i-1]+mu[i];
		}
	}
	

	// 소수 구하기
	private static void findera(int number) {
		for (int i = 2; i < era.length; i++) {
			if(era[i]==false) {
				// 결과 확인
//				System.out.println(i);
				pr.add(i);
				for (int j = i*2; j < era.length; j+=i) {
					era[j]=true;
				}
			}
		}
		
	}
	
    private static long computeSum(int a, int b) {
        long sum = 0;
        int sqrtA = (int) Math.min(Math.sqrt(a),Math.sqrt(b)) ;
        
        for (int i = 1; i <= sqrtA; i++) {
            sum += (long) (a / i) * (b / i) * mu[i];
        }
//        System.out.println(sum);
        int start=sqrtA+1;
        int end = 0;
        while(start<=a&&start<=b) {
        	int x =a/start;
        	int y =b/start;
        	end = Math.min(a / x, b /y);
//        	System.out.println("end: "+end+"   "
//        			+ "start: "+start+"  musum[end]: " +musum[end]+
//        	"musum[start]"+ musum[start-1]);
        	sum+=(long)(x)*(y)* (musum[end]-musum[start-1]);
//        	System.out.println(sum);
        	start=end+1;
        }
//        System.out.println("adfadf");
        return sum;
    }
	
	
}
