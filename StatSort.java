import java.time.LocalDateTime;
import java.util.*;
import java.lang.*;


public class MergeSort
{
	/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
//package sorter;
/**
 *
 * @author Family

     /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int upperLimit = 1000;
        int [] intBucket = new int[upperLimit];
        for (int i = 0; i < upperLimit; i++){
           intBucket[i] = (int)(Math.random()*100 + 1); 
     //      if (i%upperLimit == 0){ 
         //  debug_msg(Integer.toString(intBucket[i]));
         //int [] intBucket = {1,6,4,2,7,2,0,1,26};
        //   }
        }
        //sorterSimple(intBucket);
        sorterBucket(intBucket);    
    //  sorterBucket1(intBucket);
        }
       
    
    private static void sorterSimple(int [] intBucket) {
        debug_msg("Start sorterSimple " + LocalDateTime.now());
        Arrays.parallelSort(intBucket);
        debug_msg("End sorterSimple " + LocalDateTime.now());
    }
     private static void sorterBucket(int [] intBucket) {
        debug_msg("Start Stats " + LocalDateTime.now());
        int upperLimit = 1000;
        int buckets = (int)Math.round(upperLimit/1000);
        int [][] intBucket1 = new int[buckets][1000];       
        int iMin = intBucket[0];
        int iMax = intBucket[0];
        int iSum = 0;
        for (int i = 0; i < upperLimit; i++){
           iMin = Math.min(iMin, intBucket[i]);
           iMax = Math.max(iMax, intBucket[i]);
           iSum+=intBucket[i];      
        }
       
        int iMean;
        iMean = Math.round(iSum/upperLimit);
      //  debug_msg("End Stats " + LocalDateTime.now());
        int lowerRange = iMean - iMin;
        int upperRange = iMax - iMean;
        int iRange = iMax - iMin;
        int lowerGroups = Math.round((lowerRange)/(iRange))*10;
        lowerGroups = Math.max(1, lowerGroups);
        int upperGroups = buckets - lowerGroups;
        int [] jCounter = new int [buckets];
        int bucketSelect;
        int jSelect;
     //   debug_msg("Start Buckets " + LocalDateTime.now());
        for (int i = 0; i < upperLimit; i++){
            int iValue = intBucket[i];    
            if (iMean > iValue) {
                bucketSelect = (int)Math.ceil(lowerGroups * (iValue - iMin)/lowerRange);
            }
            else {
                bucketSelect = lowerGroups + (int)Math.ceil(upperGroups * (iValue - iMean)/upperRange);    
            }
            //debug_msg(Integer.toString(buckets) + " " + Integer.toString(bucketSelect) + " " + Integer.toString(iValue));
            
            bucketSelect = (int)((iValue - iMin)/iRange)*upperLimit/1000;
         /*   if (bucketSelect < 1000){ 
                jSelect = jCounter[bucketSelect];
            
                if (jSelect < 1000){
                    intBucket1[bucketSelect][jSelect]= (int)iValue;
                    jCounter[bucketSelect]+=1;
                } 
              }*/
        }
        //debug_msg("End Buckets " + LocalDateTime.now());
       // debug_msg("Start sorterBucket " + LocalDateTime.now());
        for (int i = 0; i < buckets; i++){
        Arrays.parallelSort(intBucket1[i
                ]);    
        }
        debug_msg("End sorterBucket " + LocalDateTime.now());
    }         
    private static void debug_msg (String printMessage){
    System.out.println(printMessage);
    }
    }
