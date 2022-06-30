/* Logic: 
Sort the array, iterate over the array if any two consecutive elements
are same return True else return False
Time Complexity - O(N log(N)), memory - O(1) (not counting the memory used to sort)
 */

class Solution {
    public boolean containsDuplicate(int[] nums) {
        boolean output = false;
        Arrays.sort(nums);
        for(int i=0; i < nums.length - 1; i++){
            if(nums[i]==nums[i+1]){
                output = true;
                break;
            }
        }
        return output;
    }
}