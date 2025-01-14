program test
    implicit none
    real :: a,b,c
    integer :: i

    open (unit = 65, file = "test_bridge.txt",status='old')
    read(65,*) a,b,c
    
    print*, a+b+c

    do i = 1, 10
        print*, i
    end do
end program test