import sys


def print_req(request):
    for req in request:
        print(req, end="  ")
    print()


def main():
    print("Enter the no. of request : ")
    n = int(input())
    print("Provide the positions to visit (max:200) : ")
    request = []
    for i in range(n):
        req_pos = int(input())
        request.append(req_pos)
    head = request[0]
    print_req(request)
    



def test():
    pass



if(len(sys.argv) > 1 and sys.argv[1] == 'test'):
    test()
else:
    main()
