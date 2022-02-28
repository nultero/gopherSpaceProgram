package main

import (
	"encoding/json"
	"fmt"
	"log"
	"math/rand"
	"net/http"
	"os"
	"population/namepkg"
	"time"
)

// TODOOOO eventually this return a JSON of the full Gopher struct

var reqs = 0

func gopher(np *namepkg.NamePool) http.HandlerFunc {
	return func(wr http.ResponseWriter, rq *http.Request) {

		k := fmt.Sprintf("gopher #%v", reqs)
		nm := np.RandomName()

		m := map[string]string{k: nm}

		bytes, err := json.Marshal(m)
		if err != nil {
			log.Fatalf("%v\n", err)
		}

		fmt.Fprintf(wr, string(bytes))
		log.Printf("gopher #%v at this station logged \n", reqs)
		reqs++
	}
}

func main() {
	port := ":8000"
	file, err := os.OpenFile("output.log", os.O_RDWR|os.O_CREATE|os.O_APPEND, 0666)
	if err != nil {
		log.Fatalf("error opening file: %v", err)
	}
	defer file.Close()

	log.SetOutput(file)
	log.Printf("server booted up, listening on port %v\n", port)

	rand.Seed(time.Now().Unix())

	np, err := namepkg.NewNamePool()
	if err != nil {
		log.Fatalf("error creating name pool: %v", err)
	}

	http.HandleFunc("/gopher", gopher(np))
	http.ListenAndServe(port, nil)
}
