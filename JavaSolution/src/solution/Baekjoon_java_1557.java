package solution;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Iterator;
/**
 * 1. 에라토스테네스 채 계산
 * 2. 소수 집합 만들기
 * 3. mu 계산
 * 4. 이분 탐색으로 조건에 맞는 수(x) 찾기
 * 5. 이분 탐색에서 구한 수는 x이하의 제곱 ㄴㄴ수가 몇 개인지이므로 x가 제곱 ㄴㄴ수가 아닐 경우 x에 1씩 빼면서 정답을 찾는다.
 */
public class Baekjoon_java_1557 {
	static int[] mu;
	static boolean[] era;
	static ArrayList<Integer> pr;
	static BufferedReader br;
	static int N;
	public static void main(String[] args) throws NumberFormatException, IOException {
		// input 받기
		br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		era = new boolean[50000];
		mu = new int[50000];
		pr  = new ArrayList<Integer>();
		// 에라토스태네스 채 계산
		era();
		// u 계산
		calculateMu();

		// 이분 탐색으로 N번째 제곱 ㄴㄴ 수가 포함되며, N+1번째 제곱 ㄴㄴ수가 포함되지 않은 수 계산
		int ed = N*2;
		int st = 0;
		int mid = (st+ed)/2;
		while(st!=ed) {
			int nthNotSquare = findNthNotSquare(mid); 
			if(N < nthNotSquare) {
				ed =mid-1;
			}else if(N >nthNotSquare) {
				st=mid+1;
			}else {
				st=mid;
				ed=mid;
			}
			mid=(int)(((double)st+(double)ed)/2);
		}
		// 위에 구한 수가 제곱 ㄴㄴ수가 아닐 경우 1씩 빼서 N번째 제곱 ㄴㄴ수를 구한다.
		int clock =1;
		while(clock ==1) {
			clock = 0;
			for (int j = 0; j < pr.size(); j++) {
				if(mid%(pr.get(j)*pr.get(j))==0) {
					clock=1;
				}
			}	
			if(clock ==1) {
				mid-=1;
			}
		}
		
		System.out.println(mid);
	}
	
	
	// 에라토스태네스 채 구하는 매서드
	static void era() {
		for (int i = 2; i < era.length; i++) {
			if(era[i]==false){
				// 소수 추가
				pr.add(i);
				for (int j = i*2; j < era.length; j+=i) {
					era[j]=true;
				}
			}
		}
		
	}
	
	// 뫼비우스 함수 값을 구하는 매서드
	static void calculateMu() {
		for (int i = 0; i < mu.length; i++) {
			mu[i]=1;
		}
		for (int i = 2; i < mu.length; i++) {
			for (int j = 0; j < pr.size(); j++) {
				if(i%pr.get(j)==0) {
					mu[i]*=-1;
					if(i%(pr.get(j)*pr.get(j))==0) {
						mu[i]=0;
					}
				}
			}
		}
	}
	
	// N이하의 수 중 제곱 ㄴㄴ수의 개수를 구하는 매서드
	static int findNthNotSquare(int number) {
		int nthNotSquareNum = 0;
		for (int i = 1; i*i <= number; i++) {
			nthNotSquareNum+=mu[i]*(number/(i*i));
		}
//		System.out.println("Number:"+number +"    NthNot: "+ nthNotSquareNum);
		return nthNotSquareNum;
	}
}
