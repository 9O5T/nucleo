program testingnucleq
    implicit none
    real :: A,B,C

    open(unit=150, file='test_variables_var.txt', status='old', action='read')

    read(150,*) A,B,C

    close(150)

    print*, A,B,C
end program testingnucleq

