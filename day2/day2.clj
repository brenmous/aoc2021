(def in (slurp "input.txt"))
(def splitted (clojure.string/split-lines in))

(defn format_commands [line]
  (clojure.string/split line #" ")
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

(def commands (map format_commands splitted))
(def xy (reduce + (map xy_command commands)))
(def z (reduce  + (map z_command commands)))
(println (* xy z))

