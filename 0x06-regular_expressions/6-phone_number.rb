#!/usr/bin/env ruby
# This ruby script will accept one argument and
# pass it to a regular expression matching method
# In this case, the script must catch 10 digit. No more no less
puts ARGV[0].scan(/^\d{10}$/)
