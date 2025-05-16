package main

import (
	"fmt"
	"math/rand"
	"sync"
)

func main() {

	c1 := make(chan int)
	c2 := make(chan int)

	go populate(c1)

	go fanOutIn(c1, c2)

	for v := range c2 {
		fmt.Println(v)
	}
}

func populate(c1 chan int) {
	for i := 0; i < 100; i++ {
		c1 <- i
	}
	close(c1)
}

func fanOutIn(c1, c2 chan int) {
	var wg sync.WaitGroup
	for v := range c1 {
		wg.Add(1)
		go func(v2 int) {
			c2 <- doTimeConsumingWork(v2)
			wg.Done()
		}(v)
	}
	wg.Wait()
	close(c2)
}

func doTimeConsumingWork(v int) int {
	return v + rand.Intn(1000)
}


================OUTPUT===========

907
995
155
88
204
401
61
75
821
293
435
952
367
694
858
40
425
381
927
289
527
394
945
688
655
51
968
535
936
803
420
763
591
957
535
931
879
933
411
70
418
696
708
675
131
304
220
129
611
313
750
991
875
634
251
79
851
577
971
998
323
833
726
132
644
309
118
900
104
132
267
102
424
1069
436
843
641
141
753
954
305
900
249
719
992
117
1078
759
107
711
950
334
809
1017
1051
245
496
418
312
808

Program exited.
