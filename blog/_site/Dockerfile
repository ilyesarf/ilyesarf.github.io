FROM jekyll/builder:3.8
VOLUME . /srv/jekyll
EXPOSE 4000
ENV GEM_HOME="/usr/local/bundle"
ENV PATH $GEM_HOME/bin:$GEM_HOME/gems/bin:$PATH
CMD bundle install
CMD jekyll serve
