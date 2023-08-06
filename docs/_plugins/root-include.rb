class RootInclude < Liquid::Tag
  def initialize(_tag_name, markup, _parse_context)
    super
    @markup = markup.strip
  end

  def render(context)
    @dir = @markup
    if (@markup.include?(" "))
      @dir = @markup.split[0]
      @lines = @markup.split[1]
      split_strings = @lines.split(':')
      start_string = split_strings[0].to_i
      end_string = split_strings[1].to_i

      expanded_path = Liquid::Template.parse(@dir).render(context)
      root_path = File.expand_path(context.registers[:site].config['source'])
      final_path = File.join(root_path, expanded_path)
      file_read_opts = context.registers[:site].file_read_opts

      read_lines_from_file(final_path, file_read_opts, start_string, end_string)
    else
      expanded_path = Liquid::Template.parse(@dir).render(context)
      root_path = File.expand_path(context.registers[:site].config['source'])
      final_path = File.join(root_path, expanded_path)
      file_read_opts = context.registers[:site].file_read_opts
      File.read(final_path, **file_read_opts)
    end

  end

  def read_lines_from_file(file_path, file_read_opts, n, m)
    lines = []
    line_number = 1

    File.foreach(file_path, **file_read_opts) do |line|
      if line_number >= n && line_number <= m
        lines << line
      elsif line_number > m
        break
      end
      line_number += 1
    end

    lines
  end
end

Liquid::Template.register_tag('root_include', RootInclude)