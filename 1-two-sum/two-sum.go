func twoSum(nums []int, target int) []int {
    hashmap := make(map[int]int)

    for i, num := range nums {
        diff := target - num
        if value, ok := hashmap[diff]; ok{
            return []int{value, i}
        }

        hashmap[num] = i
    }
    return nil;
}