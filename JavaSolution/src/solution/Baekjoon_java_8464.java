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
 * 5. 이분 탐색에서 구한 수는 x이하의 제곱수의 배수가 몇 개인지이므로 x가 제곱수의 배수가 아닐 경우 x에 1씩 빼면서 정답을 찾는다.
 */
public class Baekjoon_java_8464 {
	static long[] mu;
	static boolean[] era;
	static ArrayList<Long> pr;
	static BufferedReader br;
	static long N;
	public static void main(String[] args) throws NumberFormatException, IOException {
		// input 받기
		br = new BufferedReader(new InputStreamReader(System.in));
		N = Long.parseLong(br.readLine());
		era = new boolean[170000];
		mu = new long[170000];
		pr  = new ArrayList<Long>();
		// 에라토스태네스 채 계산
		era();
		// u 계산
		calculateMu();
//		System.out.println("전처리 완료");
		// 이분 탐색에서 구한 수는 x이하의 제곱수의 배수가 몇 개인지이므로 x가 제곱수의 배수가 아닐 경우 x에 1씩 빼면서 정답을 찾는다.
		long ed = 30000000000l;
		long st = 2*N;
		long mid = (st+ed)/2;
		while(st!=ed) {
			long nthSquare = findNthSquare(mid); 
			if(N < nthSquare) {
				ed =mid-1;
			}else if(N >nthSquare) {
				st=mid+1;
			}else {
				st=mid;
				ed=mid;
			}
			mid=(st+ed)/2;
//			System.out.println(mid);
		}
		// 이분 탐색에서 구한 수는 x이하의 제곱수의 배수가 몇 개인지이므로 x가 제곱수의 배수가 아닐 경우 x에 1씩 빼면서 정답을 찾는다.
		int clock =0;
		while(clock ==0) {
			for (int j = 0; j < pr.size(); j++) {
				if(mid%(pr.get(j)*pr.get(j))==0) {
					clock=1;
				}
			}	
			if(clock ==0) {
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
				pr.add((long)i);
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
			long tmp=i;
			for (int j = 0; j < pr.size(); j++) {
				if(tmp==1) break;
				if(tmp%pr.get(j)==0) {
					mu[i]*=-1;
					tmp=tmp/pr.get(j);
					if(tmp%pr.get(j)==0) {
						mu[i]=0;
						break;
					}
				}
			}
		}
	}
	
	// N이하의 수 중 non-squarefree수의 개수를 구하는 매서드
	static long findNthSquare(long number) {
		long nthSquareNum = 0;
		for (long i = 1; i*i <= number; i++) {
			nthSquareNum+=mu[(int)i]*(number/(i*i));
		}
		nthSquareNum=number-nthSquareNum;
//		System.out.println("Number:"+number +"    NthNot: "+ nthNotSquareNum);
		return nthSquareNum;
	}
}
