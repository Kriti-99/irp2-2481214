def count_pairs(arr, k):
    count = 0

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == k:
                count += 1

    return count


arr = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter target sum k: "))

result = count_pairs(arr, k)

print("Number of pairs:", result)
