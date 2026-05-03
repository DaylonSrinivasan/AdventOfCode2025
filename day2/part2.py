INPUT = "52-75,71615244-71792700,89451761-89562523,594077-672686,31503-39016,733-976,1-20,400309-479672,458-635,836793365-836858811,3395595155-3395672258,290-391,5168-7482,4545413413-4545538932,65590172-65702074,25-42,221412-256187,873499-1078482,118-154,68597355-68768392,102907-146478,4251706-4487069,64895-87330,8664371543-8664413195,4091-5065,537300-565631,77-115,83892238-83982935,6631446-6694349,1112-1649,7725-9776,1453397-1493799,10240-12328,15873-20410,1925-2744,4362535948-4362554186,3078725-3256936,710512-853550,279817-346202,45515-60928,3240-3952"

def parse(input: str) -> list[tuple[int, int]]:
    ranges = input.split(",")
    res = []
    for range in ranges:
        nums = range.split("-")
        res.append((int(nums[0]), int(nums[1])))
    return res

def solve(ranges: list[tuple[int, int]]) -> int:
    nums = set()
    for range in ranges:
        nums |= get_nums(range[0], range[1])
    return sum(nums)

def get_nums(start: int, end: int) -> set[int]:
    nums = set()
    for num in range(start, end+1):
        if valid(num):
            nums.add(num)
    return nums

def valid(num: int) -> bool:
    str_num = str(num)
    for length in range(1, len(str_num)):
        if len(str_num) % length != 0:
            continue
        if valid_prefix(str_num, length):
            return True
    return False

def valid_prefix(str_num: str, length: int) -> bool:
    curr = 0
    prev = str_num[0:length]
    while curr < len(str_num):
        if str_num[curr:curr+length] != prev:
            return False
        curr += length
    return True

### Main ###
print(solve(parse(INPUT)))
