package namepkg

import "math/rand"

func (np *NamePool) RandomName() string {
	odd := rand.Intn(100)
	if odd > np.odds {
		idx := rand.Intn(len(np.multiNames))
		return np.multiNames[idx]
	}

	idx := rand.Intn(len(np.names))
	return np.names[idx]
}
