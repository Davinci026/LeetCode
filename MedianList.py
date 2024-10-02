
def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    # Mescla os dois arrays em um único array ordenado
    merged = []
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    while i < len(nums1):
        merged.append(nums1[i])
        i += 1
    while j < len(nums2):
        merged.append(nums2[j])
        j += 1
    
    # Calcula a mediana
    n = len(merged)
    if n % 2 == 1:
        return merged[n // 2]
    else:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2.0

# Teste
test = findMedianSortedArrays([1, 3, 5, 7, 9, 11], [2, 8, 10])
print(test)  