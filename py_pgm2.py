test_cases = int(input())
tnob_list = []
tsob_list = []
for i in range (test_cases):
    total_no_of_buildings = int(input())
    tnob_list.append(total_no_of_buildings)
    total_size_of_buildings = [int(x) for x in input().split()]
    tsob_list.append(total_size_of_buildings)

def flood_water_volume_matrix(list_of_building_sizes, Matrix_Size):
    flood_matrix = []
    for i in range(Matrix_Size):
        flood_matrix.append([0])
        for j in range(Matrix_Size-1):
            flood_matrix[i].append(0)
    
    # for i in range(Matrix_Size):
    #     while(True):
    #         j = 0
    #         if j <= list_of_building_sizes[i]:
    #             flood_matrix[i] = 1
    #             j += 1
    #         else:
    #             break
    
    for i in range(len(flood_matrix)):
        print(i+1,flood_matrix[i],"\n")
    print("Done\n")

for i in range(test_cases):
    Size = sorted(tsob_list[i])
    flood_water_volume_matrix(tsob_list[i], Size[-1])

print(tnob_list,"\n",tsob_list)
