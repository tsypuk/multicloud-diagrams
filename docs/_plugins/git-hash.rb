module Jekyll
  class GitHashGenerator < Jekyll::Generator
    priority :high
    safe true

    def generate(site)
      hash = %x( git rev-parse --short HEAD ).strip
      full_hash = %x( git rev-parse HEAD ).strip
      tag = %x( git describe --tags --abbrev=0 ).strip
      site.data['hash'] = hash
      site.data['tag'] = tag
      site.data['full_hash'] = full_hash
      date = %x( git show -s --format=%ci)
      site.data['date'] = date
    end
  end
end

