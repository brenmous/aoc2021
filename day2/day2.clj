(defn read_input [file] 
  (def in (slurp file))
  (def splitted (clojure.string/split-lines in))
  (map (fn [line] (clojure.string/split line #" ")) splitted)
)

(defn xy_command [command]
  (case (nth command 0)
    "forward" (read-string(nth command 1))
    "down" 0
    "up" 0
  )
)

(defn z_command [command]
  (case (nth command 0)
    "forward" 0
    "down" (read-string(nth command 1))
    "up" (read-string(format "-%s" (nth command 1)))
  )
)

(def commands (read_input "input.txt"))
(def xy (reduce + (map xy_command commands)))
(def z (reduce  + (map z_command commands)))
(println (* xy z))

(def commands (read_input "input.txt"))

(def aim 
  (reductions + (map z_command commands))
)

(def xy
  (reduce + (map xy_command commands))
)

(def z
  (reduce + (map * aim (map xy_command commands)))
)
(println (* xy z))
