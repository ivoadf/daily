public class HelloWorld{
    /* Given an array of integers, write a function to determine whether the array could become non-decreasing 
    by modifying at most 1 element.
    For example, given the array [10, 5, 7], you should return true,
    since we can modify the 10 into a 1 to make the array non-decreasing.
    Given the array [10, 5, 1], you should return false, since we can't modify
    any one element to get a non-decreasing array. */
    public static Boolean decreasing_array(int[] a){
        int counter = 0;
        for(int i = 0; i < a.length - 1 && counter <= 1; i++){
            if (a[i] > a[i+1]){
                counter += 1;
            }
        }
        return counter <= 1;
    }

    public static void main(String[] args){
        System.out.println("Welcome to Java daily coding.");

        int[] a = new int[] {10,5,7};
        int[] b = new int[] {10,5,1};
        int[] c = new int[] {2,2,3,2,4};
        assert decreasing_array(a) == true;
        assert decreasing_array(b) == false;
        assert decreasing_array(c) == true;
    }
}