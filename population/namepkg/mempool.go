package namepkg

import (
	"os"
	"strings"
)

var fileNames = []string{
	"names",
	"multiNames",
}

// Struct containing the memory cache of large lists of name permutations.
type NamePool struct {
	names, multiNames []string
	odds              int // for generating a multiname
}

// Returns an instance of a pool of name strings for very quickly
// instantiating tons and tons of gophers.
func NewNamePool() (*NamePool, error) {
	np := NamePool{}
	for _, name := range fileNames {

		bytes, err := os.ReadFile(name + ".txt")
		if err != nil {
			return nil, err
		}

		s := string(bytes)
		lines := strings.Split(s, "\n")

		switch name {
		case fileNames[0]:
			np.names = lines

		case fileNames[1]:
			np.multiNames = lines
		}
	}

	fl := float64(len(np.names)) / float64(len(np.multiNames))
	np.odds = int(100.0 / fl)

	return &np, nil
}
