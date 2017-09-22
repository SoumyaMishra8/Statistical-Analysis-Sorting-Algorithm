
# Statistical-Analysis-Sorting-Algorithm
import java.time.LocalDateTime;
import java.util.*;
import java.lang.*; 
public class Sorter3 {
	public static void main(String[] args) {
		int upperLimit = 100000; 
		int [] int Bucket = new int[upperLimit];
		for (int i = 0; i < upperLimit; i++) {
			
			intBucket [i] = (int)(Math.random()*100+1);
			if (i%upperLimit == 0) {
			}
		}
		sorterSimple(intBucket);
		sortBucket(intBucket);
	}
private static void sorterSimple(int [] intBucket) {
	debug_msg("Start sorterSimple " + LocalDateTime.now()); 

	Arrays.parallelSort(intBucket);
	debug_msg("End sorterSimpole " + LocalDateTime.now());
}
private static void sorterBucket (int [] intBucket) {
	debug_msg("Start stats " + LocalDateTime.now());
g	int upperLimit = 1000000;
	int buckets = (int)Math.round(upperLimit/1000);
	int [][] intBucket1 = new int[buckets][1000];
	int iMin = intBucket[0];
	int iMax = intBucket [0];
	int iSum = 0; 
	for (int i = 0; i < upperLimit; i++) {
		iMin = Math.min(iMin, intBucket[i]); 
		iMax = Math.max(iMax, intBucket[i]);
		iSum+=intBucket[i];
  }
  int iMean; 
	iMean = Math.round(iSum/upperLimit);
 	int lowerRange = iMean - iMin; 
	int upperRange = iMax - iMean; 
	int iRange = iMax - iMean; 
	int lowerGroups = Math.round((lowerRange/(iRange))*10; 
	lowerGroups = Math.max(1, lowerGroups); 
	int upperGroups = buckets - lowerGroups;
	int [] jCounter = new int [buckets]; 
	int bucketSelect; 
	int jSelect;
	for (int i = 0; i < upperLimit; i++) {
		int iValue = intBucket[i];
		if (iMean > iValue) {
			bucketSelect = (int)Math.ceil(lowerGroups* (iValue - iMin)/lowerRange);
		}
		else {
			bucketSelect = lowerGroups + (int)Math.ceil(upperGroups * (iValue - iMean)/upperRange);
		}
	if (bucketSelect < 1000) { 
		jSelect = jCounter[bucketSelect];
		if (jSelect < 1000) {
			intBucket1[bucketSelect][jSelect] = (int)iValue; 
			jCounter[bucketSelect]+=1;
    }
  }
}
	for (int i = 0; i < buckets; i++) {
		System.out.println(intBucket[i]);
		Arrays.parallelSort(intBucket1[i]);
  }
  debug_msg("End sorterBucket " + LocalDateTime.now());
	for (int b = -; b < upperLimit; b++) {
System.out.print(intBucket[b]+", ");
}
	private static void debug_msg (String printMessage) {
	System.out.println(printMessage);
  }
}
		


 		

		
