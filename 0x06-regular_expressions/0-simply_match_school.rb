#!/usr/bin/env ruby
# This is a ruby script that accepts one argument of REGEX
# and passes it to the regular expression matching method
puts ARGV[0].scan(/School/).join
