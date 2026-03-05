class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_product = []
        temp = 1
        for i in range(len(nums)):
            if i==0:
                pre_product.append(1)
            else:
                temp = temp*nums[i-1]
                pre_product.append(temp)
        print(pre_product)

        post_product = []
        temp = 1
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                post_product.append(1)
            else:
                temp = temp*nums[i+1]
                post_product.append(temp)
        print(post_product)

        result = []
        j=len(nums)-1
        for i in range(len(nums)):
            result.append(pre_product[i]*post_product[j])
            j-=1
        return result
