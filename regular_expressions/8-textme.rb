#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=from:)(.\d+)|(?<=to:)(.\d+)|(?<=flags:)([0-9|:|-]+)/).join(",")
