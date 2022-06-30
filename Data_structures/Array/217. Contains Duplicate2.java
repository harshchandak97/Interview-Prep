/* Logic: 
Create a set, add elements to it. If an element is already present in
the set return True else return False
Time Complexity - O(N), memory - O(N) (created a set) 
*/

class Solution {
    public boolean containsDuplicate(int[] nums) {
        boolean output = false;
        Set<Integer> numberSet = new HashSet<Integer>();
        for (int i=0; i<nums.length; i++){
            if (numberSet.contains(nums[i])){
                output = true;
                break;
            }
            else{
                numberSet.add(nums[i]);
            }
        }
        return output;
    }
}