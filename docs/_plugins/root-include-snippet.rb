class RootIncludeSnippet < Liquid::Tag
  def initialize(_tag_name, markup, _parse_context)
    super
    @markup = markup.strip
  end

  def render(context)
    @func = ''
    @dir = @markup
    if (@markup.include?(" "))
      @dir = @markup.split[0]
      @func = @markup.split[1]
    end

    expanded_path = Liquid::Template.parse(@dir).render(context)
    root_path = File.expand_path(context.registers[:site].config['source'])
    final_path = File.join(root_path, expanded_path)
    file_read_opts = context.registers[:site].file_read_opts

    read_lines_from_file(final_path, file_read_opts, @func)
  end

  def read_lines_from_file(file_path, file_read_opts, func_name)
    lines = []
    in_section = false
    in_func = false
    func = 'def test_' + func_name

    File.foreach(file_path, **file_read_opts) do |line|
      # print(file_path)
      if line.include?(func)
        in_func = true
      end

      if in_func
        if line.include?('# given')
          in_section = true
        elsif line.include?('# then')
          break
        end
        # line.sub!(/^\t{2}/, "")
        line.sub!(/^ {8}/, "")
        lines << line if in_section and in_func
      end
    end
    # print(lines)
    # lines << '# then'
    lines.pop
    lines
  end
end

Liquid::Template.register_tag('root_include_snippet', RootIncludeSnippet)
