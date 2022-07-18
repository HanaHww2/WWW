import ("math")
    
func solution(progresses []int, speeds []int) []int {
    var releaseDates []int
    for i := 0; i <len(progresses); i++ {
        releaseDate := math.Ceil(float64(100-progresses[i])/float64(speeds[i]))
        releaseDates = append(releaseDates, int(releaseDate))
    }
    var result []int
    var tmp = 0
    var tmpR int
    tmpR = releaseDates[0]
    for i := range releaseDates {
        if releaseDates[i] <= tmpR {
            tmp += 1
        } else {
            result = append(result, tmp)
            tmp = 1
            tmpR = releaseDates[i]
        }
        
    }
    result = append(result,tmp)
    return result
}
