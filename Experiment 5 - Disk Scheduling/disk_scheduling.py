import sys


def print_req(request_queue):
    for req in request_queue:
        print(req, end="  ")
    print()

def head_movement_path(head_movement):
    print()
    for item in head_movement:
        print(item, end=" -> ")
    print("END")
    print()


def fcfs(request_queue, head):
    movement = 0
    prev_head = head
    head_movement= []
    head_movement.append(head)
    for req in request_queue:
        movement += abs(req - prev_head)
        head_movement.append(req)
        prev_head = req
    print("\n----------FCFS Scheduling----------")
    head_movement_path(head_movement)
    print("Total Head Movement = ", movement)
    print("-----------------------------------\n")

def scan(req_queue, head):
    request_queue = req_queue[:]
    prev_head = head
    movement = 0
    head_movement = []
    head_movement.append(head)
    for req in range(head, 200):
        if req in request_queue:
            movement += abs(req - prev_head)
            prev_head = req
            head_movement.append(req)
            request_queue.remove(req)
    for req in range(200, 0, -1):
        if req in request_queue:
            movement += abs(req - prev_head)
            prev_head = req
            head_movement.append(req)
            request_queue.remove(req)

    print("\n----------SCAN Scheduling----------")
    head_movement_path(head_movement)
    print("Total Head Movement : ", movement)
    print("-----------------------------------\n")

def cscan(req_queue, head):
    request_queue = req_queue[:]
    prev_head = head
    movement = 0
    head_movement = []
    head_movement.append(head)
    for req in range(head, 200):
        if req in request_queue:
            movement += abs(req - prev_head)
            prev_head = req
            head_movement.append(req)
            request_queue.remove(req)
    for req in range(0, 200):
        if req in request_queue:
            movement += abs(req - prev_head)
            prev_head = req
            head_movement.append(req)
            request_queue.remove(req)

    print("\n----------CSCAN Scheduling----------")
    head_movement_path(head_movement)
    print("Total Head Movement : ", movement)
    print("-----------------------------------\n")



def main():
    print("Enter the no. of request : ")
    n = int(input())

    print("Enter Head Position : ")
    head = int(input())

    print("Provide the positions to visit (max:200) : ")
    request_queue = [int(x) for x in input().split()]

    fcfs(request_queue, head)
    scan(request_queue, head)
    cscan(request_queue, head)
    



def test():
    pass



if(len(sys.argv) > 1 and sys.argv[1] == 'test'):
    test()
else:
    main()
