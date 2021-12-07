(defn get_crabs [file]
  (map read-string (clojure.string/split (slurp file) #","))
)

(defn abs [n] (max n (- n)))

(defn moves [end]
  (if (<= end 1) end (+ end (moves (- end 1))))
)

(defn moves2 [end]
  (reduce + (range 1 (+ 1 end)))
)

(defn moves3 [end]
  (/ (* end (+ end 1)) 2)
)

(defn fuel_costing1 [crab pos]
  (abs (- crab pos))
)

(defn fuel_costing2 [crab pos]
  (moves3 (abs(- crab pos)))
)

  
(defn part1 [crabs]
  (for [pos (range 1 (+ (apply max crabs) 1))]
    (reduce + (map (fn [crab] (fuel_costing1 crab pos)) crabs))
  )
)

(defn part2 [crabs]
  (for [pos (range 1 (+ (apply max crabs) 1))]
    (reduce + (map (fn [crab] (fuel_costing2 crab pos)) crabs))
  )
)

(def crabs (get_crabs "input.txt"))
(println (apply min (part1 crabs)))
(println (apply min (part2 crabs)))
