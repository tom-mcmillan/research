This is the code from the page https://openai.github.io/openai-agents-python/ which i like the look and feel of. This page may be more complicated than ours, so i'm sharing it here simply because i like that each page has a unique table of contents on the right, which i believe is referred to as a secondary sidebar. I also like the primary sidebar, and the content layout, and the colors and fonts. It's for reference when building our secondary sidebar. 

```

<body dir="ltr" data-md-color-scheme="default" data-md-color-primary="black" data-md-color-accent="indigo">
  
    
    <input class="md-toggle" data-md-toggle="drawer" type="checkbox" id="__drawer" autocomplete="off">
    <input class="md-toggle" data-md-toggle="search" type="checkbox" id="__search" autocomplete="off">
    <label class="md-overlay" for="__drawer"></label>
    <div data-md-component="skip">
      
        
        <a href="#quickstart" class="md-skip">
          Skip to content
        </a>
      
    </div>
    <div data-md-component="announce">
      
    </div>
    
    
      

  

<header class="md-header md-header--shadow" data-md-component="header">
  <nav class="md-header__inner md-grid" aria-label="Header">
    <a href=".." title="OpenAI Agents SDK" class="md-header__button md-logo" aria-label="OpenAI Agents SDK" data-md-component="logo">
      
  <img src="../assets/logo.svg" alt="logo">

    </a>
    <label class="md-header__button md-icon" for="__drawer">
      
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M3 6h18v2H3zm0 5h18v2H3zm0 5h18v2H3z"></path></svg>
    </label>
    <div class="md-header__title" data-md-component="header-title">
      <div class="md-header__ellipsis">
        <div class="md-header__topic">
          <span class="md-ellipsis">
            OpenAI Agents SDK
          </span>
        </div>
        <div class="md-header__topic" data-md-component="header-topic">
          <span class="md-ellipsis">
            
              Quickstart
            
          </span>
        </div>
      </div>
    </div>
    
      
    
    
    
      <div class="md-header__option">
  <div class="md-select">
    
    <button class="md-header__button md-icon" aria-label="Select language">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="m12.87 15.07-2.54-2.51.03-.03A17.5 17.5 0 0 0 14.07 6H17V4h-7V2H8v2H1v2h11.17C11.5 7.92 10.44 9.75 9 11.35 8.07 10.32 7.3 9.19 6.69 8h-2c.73 1.63 1.73 3.17 2.98 4.56l-5.09 5.02L4 19l5-5 3.11 3.11zM18.5 10h-2L12 22h2l1.12-3h4.75L21 22h2zm-2.62 7 1.62-4.33L19.12 17z"></path></svg>
    </button>
    <div class="md-select__inner">
      <ul class="md-select__list">
        
          <li class="md-select__item">
            <a href="./" hreflang="en" class="md-select__link">
              English
            </a>
          </li>
        
          <li class="md-select__item">
            <a href="../ja/quickstart/" hreflang="ja" class="md-select__link">
              日本語
            </a>
          </li>
        
      </ul>
    </div>
  </div>
</div>
    
    
      
      
        <label class="md-header__button md-icon" for="__search">
          
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9.5 3A6.5 6.5 0 0 1 16 9.5c0 1.61-.59 3.09-1.56 4.23l.27.27h.79l5 5-1.5 1.5-5-5v-.79l-.27-.27A6.52 6.52 0 0 1 9.5 16 6.5 6.5 0 0 1 3 9.5 6.5 6.5 0 0 1 9.5 3m0 2C7 5 5 7 5 9.5S7 14 9.5 14 14 12 14 9.5 12 5 9.5 5"></path></svg>
        </label>
        <div class="md-search" data-md-component="search" role="dialog">
  <label class="md-search__overlay" for="__search"></label>
  <div class="md-search__inner" role="search">
    <form class="md-search__form" name="search">
      <input type="text" class="md-search__input" name="query" aria-label="Search" placeholder="Search" autocapitalize="off" autocorrect="off" autocomplete="off" spellcheck="false" data-md-component="search-query" required="">
      <label class="md-search__icon md-icon" for="__search">
        
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9.5 3A6.5 6.5 0 0 1 16 9.5c0 1.61-.59 3.09-1.56 4.23l.27.27h.79l5 5-1.5 1.5-5-5v-.79l-.27-.27A6.52 6.52 0 0 1 9.5 16 6.5 6.5 0 0 1 3 9.5 6.5 6.5 0 0 1 9.5 3m0 2C7 5 5 7 5 9.5S7 14 9.5 14 14 12 14 9.5 12 5 9.5 5"></path></svg>
        
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M20 11v2H8l5.5 5.5-1.42 1.42L4.16 12l7.92-7.92L13.5 5.5 8 11z"></path></svg>
      </label>
      <nav class="md-search__options" aria-label="Search">
        
        <button type="reset" class="md-search__icon md-icon" title="Clear" aria-label="Clear" tabindex="-1">
          
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 6.41 17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"></path></svg>
        </button>
      </nav>
      
    </form>
    <div class="md-search__output">
      <div class="md-search__scrollwrap" tabindex="0">
        <div class="md-search-result" data-md-component="search-result">
          <div class="md-search-result__meta">Type to start searching</div>
          <ol class="md-search-result__list" role="presentation"></ol>
        </div>
      </div>
    </div>
  </div>
</div>
      
    
    
      <div class="md-header__source">
        <a href="https://github.com/openai/openai-agents-python" title="Go to repository" class="md-source" data-md-component="source">
  <div class="md-source__icon md-icon">
    
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2024 Fonticons, Inc.--><path d="M439.55 236.05 244 40.45a28.87 28.87 0 0 0-40.81 0l-40.66 40.63 51.52 51.52c27.06-9.14 52.68 16.77 43.39 43.68l49.66 49.66c34.23-11.8 61.18 31 35.47 56.69-26.49 26.49-70.21-2.87-56-37.34L240.22 199v121.85c25.3 12.54 22.26 41.85 9.08 55a34.34 34.34 0 0 1-48.55 0c-17.57-17.6-11.07-46.91 11.25-56v-123c-20.8-8.51-24.6-30.74-18.64-45L142.57 101 8.45 235.14a28.86 28.86 0 0 0 0 40.81l195.61 195.6a28.86 28.86 0 0 0 40.8 0l194.69-194.69a28.86 28.86 0 0 0 0-40.81"></path></svg>
  </div>
  <div class="md-source__repository md-source__repository--active">
    openai-agents-python
  <ul class="md-source__facts"><li class="md-source__fact md-source__fact--version">v0.0.16</li><li class="md-source__fact md-source__fact--stars">10.9k</li><li class="md-source__fact md-source__fact--forks">1.5k</li></ul></div>
</a>
      </div>
    
  </nav>
  
</header>
    
    <div class="md-container" data-md-component="container">
      
      
        
          
        
      
      <main class="md-main" data-md-component="main">
        <div class="md-main__inner md-grid">
          
            
              
              <div class="md-sidebar md-sidebar--primary" data-md-component="sidebar" data-md-type="navigation" style="top: 48px;">
                <div class="md-sidebar__scrollwrap" style="height: 921px;">
                  <div class="md-sidebar__inner">
                    



<nav class="md-nav md-nav--primary" aria-label="Navigation" data-md-level="0">
  <label class="md-nav__title" for="__drawer">
    <a href=".." title="OpenAI Agents SDK" class="md-nav__button md-logo" aria-label="OpenAI Agents SDK" data-md-component="logo">
      
  <img src="../assets/logo.svg" alt="logo">

    </a>
    OpenAI Agents SDK
  </label>
  
    <div class="md-nav__source">
      <a href="https://github.com/openai/openai-agents-python" title="Go to repository" class="md-source" data-md-component="source">
  <div class="md-source__icon md-icon">
    
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2024 Fonticons, Inc.--><path d="M439.55 236.05 244 40.45a28.87 28.87 0 0 0-40.81 0l-40.66 40.63 51.52 51.52c27.06-9.14 52.68 16.77 43.39 43.68l49.66 49.66c34.23-11.8 61.18 31 35.47 56.69-26.49 26.49-70.21-2.87-56-37.34L240.22 199v121.85c25.3 12.54 22.26 41.85 9.08 55a34.34 34.34 0 0 1-48.55 0c-17.57-17.6-11.07-46.91 11.25-56v-123c-20.8-8.51-24.6-30.74-18.64-45L142.57 101 8.45 235.14a28.86 28.86 0 0 0 0 40.81l195.61 195.6a28.86 28.86 0 0 0 40.8 0l194.69-194.69a28.86 28.86 0 0 0 0-40.81"></path></svg>
  </div>
  <div class="md-source__repository md-source__repository--active">
    openai-agents-python
  <ul class="md-source__facts"><li class="md-source__fact md-source__fact--version">v0.0.16</li><li class="md-source__fact md-source__fact--stars">10.9k</li><li class="md-source__fact md-source__fact--forks">1.5k</li></ul></div>
</a>
    </div>
  
  <ul class="md-nav__list">
    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href=".." class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Intro
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
    
  
  
  
    <li class="md-nav__item md-nav__item--active">
      
      <input class="md-nav__toggle md-toggle" type="checkbox" id="__toc">
      
      
        
      
      
        <label class="md-nav__link md-nav__link--active" for="__toc">
          
  
  
  <span class="md-ellipsis">
    Quickstart
    
  </span>
  

          <span class="md-nav__icon md-icon"></span>
        </label>
      
      <a href="./" class="md-nav__link md-nav__link--active">
        
  
  
  <span class="md-ellipsis">
    Quickstart
    
  </span>
  

      </a>
      
        

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
    
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#create-a-project-and-virtual-environment" class="md-nav__link">
    <span class="md-ellipsis">
      Create a project and virtual environment
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Create a project and virtual environment">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#activate-the-virtual-environment" class="md-nav__link">
    <span class="md-ellipsis">
      Activate the virtual environment
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#install-the-agents-sdk" class="md-nav__link">
    <span class="md-ellipsis">
      Install the Agents SDK
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#set-an-openai-api-key" class="md-nav__link">
    <span class="md-ellipsis">
      Set an OpenAI API key
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#create-your-first-agent" class="md-nav__link">
    <span class="md-ellipsis">
      Create your first agent
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#add-a-few-more-agents" class="md-nav__link">
    <span class="md-ellipsis">
      Add a few more agents
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#define-your-handoffs" class="md-nav__link">
    <span class="md-ellipsis">
      Define your handoffs
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#run-the-agent-orchestration" class="md-nav__link">
    <span class="md-ellipsis">
      Run the agent orchestration
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#add-a-guardrail" class="md-nav__link">
    <span class="md-ellipsis">
      Add a guardrail
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#put-it-all-together" class="md-nav__link">
    <span class="md-ellipsis">
      Put it all together
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#view-your-traces" class="md-nav__link">
    <span class="md-ellipsis">
      View your traces
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#next-steps" class="md-nav__link">
    <span class="md-ellipsis">
      Next steps
    </span>
  </a>
  
</li>
      
    </ul>
  
</nav>
      
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Examples
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    
    
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--section md-nav__item--nested">
      
        
        
          
        
        <input class="md-nav__toggle md-toggle" type="checkbox" id="__nav_4">
        
          
          <label class="md-nav__link" for="__nav_4" id="__nav_4_label" tabindex="">
            
  
  
  <span class="md-ellipsis">
    Documentation
    
  </span>
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_4_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_4">
            <span class="md-nav__icon md-icon"></span>
            Documentation
          </label>
          <ul class="md-nav__list">
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../agents/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Agents
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../running_agents/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Running agents
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../results/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Results
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../streaming/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Streaming
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../tools/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../mcp/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Model context protocol (MCP)
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../handoffs/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Handoffs
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../tracing/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Tracing
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../context/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Context management
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../guardrails/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Guardrails
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../multi_agent/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Orchestrating multiple agents
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    
    
    
    
      
    
    
    <li class="md-nav__item md-nav__item--nested">
      
        
        
          
        
        <input class="md-nav__toggle md-toggle md-toggle--indeterminate" type="checkbox" id="__nav_4_12">
        
          
          <label class="md-nav__link" for="__nav_4_12" id="__nav_4_12_label" tabindex="0">
            
  
  
  <span class="md-ellipsis">
    Models
    
  </span>
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="2" aria-labelledby="__nav_4_12_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_4_12">
            <span class="md-nav__icon md-icon"></span>
            Models
          </label>
          <ul class="md-nav__list">
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Models
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/litellm/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Using any model via LiteLLM
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../config/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Configuring the SDK
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../visualization/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Agent Visualization
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    
    
    
    
      
    
    
    <li class="md-nav__item md-nav__item--nested">
      
        
        
          
        
        <input class="md-nav__toggle md-toggle md-toggle--indeterminate" type="checkbox" id="__nav_4_15">
        
          
          <label class="md-nav__link" for="__nav_4_15" id="__nav_4_15_label" tabindex="0">
            
  
  
  <span class="md-ellipsis">
    Voice agents
    
  </span>
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="2" aria-labelledby="__nav_4_15_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_4_15">
            <span class="md-nav__icon md-icon"></span>
            Voice agents
          </label>
          <ul class="md-nav__list">
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../voice/quickstart/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Quickstart
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../voice/pipeline/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Pipelines and workflows
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../voice/tracing/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Tracing
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
      
      
  
  
  
  
    
    
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--section md-nav__item--nested">
      
        
        
          
        
        <input class="md-nav__toggle md-toggle md-toggle--indeterminate" type="checkbox" id="__nav_5">
        
          
          <label class="md-nav__link" for="__nav_5" id="__nav_5_label" tabindex="">
            
  
  
  <span class="md-ellipsis">
    API Reference
    
  </span>
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_5_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_5">
            <span class="md-nav__icon md-icon"></span>
            API Reference
          </label>
          <ul class="md-nav__list">
            
              
                
  
  
  
  
    
    
    
    
      
    
    
    <li class="md-nav__item md-nav__item--nested">
      
        
        
          
        
        <input class="md-nav__toggle md-toggle md-toggle--indeterminate" type="checkbox" id="__nav_5_1">
        
          
          <label class="md-nav__link" for="__nav_5_1" id="__nav_5_1_label" tabindex="0">
            
  
  
  <span class="md-ellipsis">
    Agents
    
  </span>
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="2" aria-labelledby="__nav_5_1_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_5_1">
            <span class="md-nav__icon md-icon"></span>
            Agents
          </label>
          <ul class="md-nav__list">
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Agents module
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/agent/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Agents
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/run/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Runner
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/tool/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/result/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Results
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/stream_events/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Streaming events
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/handoffs/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Handoffs
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/lifecycle/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Lifecycle
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/items/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Items
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/run_context/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Run context
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/usage/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Usage
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/exceptions/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/guardrail/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Guardrails
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/model_settings/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Model settings
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/agent_output/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Agent output
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/function_schema/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Function schema
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/models/interface/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Model interface
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/models/openai_chatcompletions/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    OpenAI Chat Completions model
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/models/openai_responses/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    OpenAI Responses model
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/mcp/server/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    MCP Servers
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/mcp/util/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    MCP Util
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    
    
    
    
      
    
    
    <li class="md-nav__item md-nav__item--nested">
      
        
        
          
        
        <input class="md-nav__toggle md-toggle md-toggle--indeterminate" type="checkbox" id="__nav_5_2">
        
          
          <label class="md-nav__link" for="__nav_5_2" id="__nav_5_2_label" tabindex="0">
            
  
  
  <span class="md-ellipsis">
    Tracing
    
  </span>
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="2" aria-labelledby="__nav_5_2_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_5_2">
            <span class="md-nav__icon md-icon"></span>
            Tracing
          </label>
          <ul class="md-nav__list">
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/tracing/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Tracing module
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/tracing/create/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Creating traces/spans
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/tracing/traces/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Traces
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/tracing/spans/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Spans
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/tracing/processor_interface/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Processor interface
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/tracing/processors/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Processors
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/tracing/scope/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Scope
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/tracing/setup/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Setup
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/tracing/span_data/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Span data
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/tracing/util/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Util
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    
    
    
    
      
    
    
    <li class="md-nav__item md-nav__item--nested">
      
        
        
          
        
        <input class="md-nav__toggle md-toggle md-toggle--indeterminate" type="checkbox" id="__nav_5_3">
        
          
          <label class="md-nav__link" for="__nav_5_3" id="__nav_5_3_label" tabindex="0">
            
  
  
  <span class="md-ellipsis">
    Voice
    
  </span>
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="2" aria-labelledby="__nav_5_3_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_5_3">
            <span class="md-nav__icon md-icon"></span>
            Voice
          </label>
          <ul class="md-nav__list">
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/voice/pipeline/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Pipeline
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/voice/workflow/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Workflow
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/voice/input/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Input
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/voice/result/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Result
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/voice/pipeline_config/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Pipeline Config
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/voice/events/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Events
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/voice/exceptions/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/voice/model/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Model
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/voice/utils/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Utils
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/voice/models/openai_provider/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    OpenAIVoiceModelProvider
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/voice/models/openai_stt/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    OpenAI STT
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/voice/models/openai_tts/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    OpenAI TTS
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    
    
    
    
      
    
    
    <li class="md-nav__item md-nav__item--nested">
      
        
        
          
        
        <input class="md-nav__toggle md-toggle md-toggle--indeterminate" type="checkbox" id="__nav_5_4">
        
          
          <label class="md-nav__link" for="__nav_5_4" id="__nav_5_4_label" tabindex="0">
            
  
  
  <span class="md-ellipsis">
    Extensions
    
  </span>
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="2" aria-labelledby="__nav_5_4_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_5_4">
            <span class="md-nav__icon md-icon"></span>
            Extensions
          </label>
          <ul class="md-nav__list">
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/extensions/handoff_filters/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Handoff filters
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/extensions/handoff_prompt/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    Handoff prompt
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../ref/extensions/litellm/" class="md-nav__link">
        
  
  
  <span class="md-ellipsis">
    LiteLLM Models
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
  </ul>
</nav>
                  </div>
                </div>
              </div>
            
            
              
              <div class="md-sidebar md-sidebar--secondary" data-md-component="sidebar" data-md-type="toc" style="top: 48px;">
                <div class="md-sidebar__scrollwrap" style="height: 921px;">
                  <div class="md-sidebar__inner">
                    

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
    
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#create-a-project-and-virtual-environment" class="md-nav__link">
    <span class="md-ellipsis">
      Create a project and virtual environment
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Create a project and virtual environment">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#activate-the-virtual-environment" class="md-nav__link">
    <span class="md-ellipsis">
      Activate the virtual environment
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#install-the-agents-sdk" class="md-nav__link">
    <span class="md-ellipsis">
      Install the Agents SDK
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#set-an-openai-api-key" class="md-nav__link">
    <span class="md-ellipsis">
      Set an OpenAI API key
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#create-your-first-agent" class="md-nav__link">
    <span class="md-ellipsis">
      Create your first agent
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#add-a-few-more-agents" class="md-nav__link">
    <span class="md-ellipsis">
      Add a few more agents
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#define-your-handoffs" class="md-nav__link">
    <span class="md-ellipsis">
      Define your handoffs
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#run-the-agent-orchestration" class="md-nav__link">
    <span class="md-ellipsis">
      Run the agent orchestration
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#add-a-guardrail" class="md-nav__link">
    <span class="md-ellipsis">
      Add a guardrail
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#put-it-all-together" class="md-nav__link">
    <span class="md-ellipsis">
      Put it all together
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#view-your-traces" class="md-nav__link">
    <span class="md-ellipsis">
      View your traces
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#next-steps" class="md-nav__link">
    <span class="md-ellipsis">
      Next steps
    </span>
  </a>
  
</li>
      
    </ul>
  
</nav>
                  </div>
                </div>
              </div>
            
          
          
            <div class="md-content" data-md-component="content">
              <article class="md-content__inner md-typeset">
                
                  


  
  


<h1 id="quickstart">Quickstart</h1>
<h2 id="create-a-project-and-virtual-environment">Create a project and virtual environment</h2>
<p>You'll only need to do this once.</p>
<div class="language-bash highlight"><pre id="__code_0"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_0 > code"></button><code class="md-code__content"><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="#__codelineno-0-1"></a>mkdir<span class="w"> </span>my_project
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="#__codelineno-0-2"></a><span class="nb">cd</span><span class="w"> </span>my_project
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="#__codelineno-0-3"></a>python<span class="w"> </span>-m<span class="w"> </span>venv<span class="w"> </span>.venv
</span></code></pre></div>
<h3 id="activate-the-virtual-environment">Activate the virtual environment</h3>
<p>Do this every time you start a new terminal session.</p>
<div class="language-bash highlight"><pre id="__code_1"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_1 > code"></button><code class="md-code__content"><span id="__span-1-1"><a id="__codelineno-1-1" name="__codelineno-1-1" href="#__codelineno-1-1"></a><span class="nb">source</span><span class="w"> </span>.venv/bin/activate
</span></code></pre></div>
<h3 id="install-the-agents-sdk">Install the Agents SDK</h3>
<div class="language-bash highlight"><pre id="__code_2"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_2 > code"></button><code class="md-code__content"><span id="__span-2-1"><a id="__codelineno-2-1" name="__codelineno-2-1" href="#__codelineno-2-1"></a>pip<span class="w"> </span>install<span class="w"> </span>openai-agents<span class="w"> </span><span class="c1"># or `uv add openai-agents`, etc</span>
</span></code></pre></div>
<h3 id="set-an-openai-api-key">Set an OpenAI API key</h3>
<p>If you don't have one, follow <a href="https://platform.openai.com/docs/quickstart#create-and-export-an-api-key">these instructions</a> to create an OpenAI API key.</p>
<div class="language-bash highlight"><pre id="__code_3"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_3 > code"></button><code class="md-code__content"><span id="__span-3-1"><a id="__codelineno-3-1" name="__codelineno-3-1" href="#__codelineno-3-1"></a><span class="nb">export</span><span class="w"> </span><span class="nv">OPENAI_API_KEY</span><span class="o">=</span>sk-...
</span></code></pre></div>
<h2 id="create-your-first-agent">Create your first agent</h2>
<p>Agents are defined with instructions, a name, and optional config (such as <code>model_config</code>)</p>
<div class="language-python highlight"><pre id="__code_4"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_4 > code"></button><code class="md-code__content" tabindex="0"><span id="__span-4-1"><a id="__codelineno-4-1" name="__codelineno-4-1" href="#__codelineno-4-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">agents</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
</span><span id="__span-4-2"><a id="__codelineno-4-2" name="__codelineno-4-2" href="#__codelineno-4-2"></a>
</span><span id="__span-4-3"><a id="__codelineno-4-3" name="__codelineno-4-3" href="#__codelineno-4-3"></a><span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span>
</span><span id="__span-4-4"><a id="__codelineno-4-4" name="__codelineno-4-4" href="#__codelineno-4-4"></a>    <span class="n">name</span><span class="o">=</span><span class="s2">"Math Tutor"</span><span class="p">,</span>
</span><span id="__span-4-5"><a id="__codelineno-4-5" name="__codelineno-4-5" href="#__codelineno-4-5"></a>    <span class="n">instructions</span><span class="o">=</span><span class="s2">"You provide help with math problems. Explain your reasoning at each step and include examples"</span><span class="p">,</span>
</span><span id="__span-4-6"><a id="__codelineno-4-6" name="__codelineno-4-6" href="#__codelineno-4-6"></a><span class="p">)</span>
</span></code></pre></div>
<h2 id="add-a-few-more-agents">Add a few more agents</h2>
<p>Additional agents can be defined in the same way. <code>handoff_descriptions</code> provide additional context for determining handoff routing</p>
<div class="language-python highlight"><pre id="__code_5"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_5 > code"></button><code class="md-code__content" tabindex="0"><span id="__span-5-1"><a id="__codelineno-5-1" name="__codelineno-5-1" href="#__codelineno-5-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">agents</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
</span><span id="__span-5-2"><a id="__codelineno-5-2" name="__codelineno-5-2" href="#__codelineno-5-2"></a>
</span><span id="__span-5-3"><a id="__codelineno-5-3" name="__codelineno-5-3" href="#__codelineno-5-3"></a><span class="n">history_tutor_agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span>
</span><span id="__span-5-4"><a id="__codelineno-5-4" name="__codelineno-5-4" href="#__codelineno-5-4"></a>    <span class="n">name</span><span class="o">=</span><span class="s2">"History Tutor"</span><span class="p">,</span>
</span><span id="__span-5-5"><a id="__codelineno-5-5" name="__codelineno-5-5" href="#__codelineno-5-5"></a>    <span class="n">handoff_description</span><span class="o">=</span><span class="s2">"Specialist agent for historical questions"</span><span class="p">,</span>
</span><span id="__span-5-6"><a id="__codelineno-5-6" name="__codelineno-5-6" href="#__codelineno-5-6"></a>    <span class="n">instructions</span><span class="o">=</span><span class="s2">"You provide assistance with historical queries. Explain important events and context clearly."</span><span class="p">,</span>
</span><span id="__span-5-7"><a id="__codelineno-5-7" name="__codelineno-5-7" href="#__codelineno-5-7"></a><span class="p">)</span>
</span><span id="__span-5-8"><a id="__codelineno-5-8" name="__codelineno-5-8" href="#__codelineno-5-8"></a>
</span><span id="__span-5-9"><a id="__codelineno-5-9" name="__codelineno-5-9" href="#__codelineno-5-9"></a><span class="n">math_tutor_agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span>
</span><span id="__span-5-10"><a id="__codelineno-5-10" name="__codelineno-5-10" href="#__codelineno-5-10"></a>    <span class="n">name</span><span class="o">=</span><span class="s2">"Math Tutor"</span><span class="p">,</span>
</span><span id="__span-5-11"><a id="__codelineno-5-11" name="__codelineno-5-11" href="#__codelineno-5-11"></a>    <span class="n">handoff_description</span><span class="o">=</span><span class="s2">"Specialist agent for math questions"</span><span class="p">,</span>
</span><span id="__span-5-12"><a id="__codelineno-5-12" name="__codelineno-5-12" href="#__codelineno-5-12"></a>    <span class="n">instructions</span><span class="o">=</span><span class="s2">"You provide help with math problems. Explain your reasoning at each step and include examples"</span><span class="p">,</span>
</span><span id="__span-5-13"><a id="__codelineno-5-13" name="__codelineno-5-13" href="#__codelineno-5-13"></a><span class="p">)</span>
</span></code></pre></div>
<h2 id="define-your-handoffs">Define your handoffs</h2>
<p>On each agent, you can define an inventory of outgoing handoff options that the agent can choose from to decide how to make progress on their task.</p>
<div class="language-python highlight"><pre id="__code_6"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_6 > code"></button><code class="md-code__content" tabindex="0"><span id="__span-6-1"><a id="__codelineno-6-1" name="__codelineno-6-1" href="#__codelineno-6-1"></a><span class="n">triage_agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span>
</span><span id="__span-6-2"><a id="__codelineno-6-2" name="__codelineno-6-2" href="#__codelineno-6-2"></a>    <span class="n">name</span><span class="o">=</span><span class="s2">"Triage Agent"</span><span class="p">,</span>
</span><span id="__span-6-3"><a id="__codelineno-6-3" name="__codelineno-6-3" href="#__codelineno-6-3"></a>    <span class="n">instructions</span><span class="o">=</span><span class="s2">"You determine which agent to use based on the user's homework question"</span><span class="p">,</span>
</span><span id="__span-6-4"><a id="__codelineno-6-4" name="__codelineno-6-4" href="#__codelineno-6-4"></a>    <span class="n">handoffs</span><span class="o">=</span><span class="p">[</span><span class="n">history_tutor_agent</span><span class="p">,</span> <span class="n">math_tutor_agent</span><span class="p">]</span>
</span><span id="__span-6-5"><a id="__codelineno-6-5" name="__codelineno-6-5" href="#__codelineno-6-5"></a><span class="p">)</span>
</span></code></pre></div>
<h2 id="run-the-agent-orchestration">Run the agent orchestration</h2>
<p>Let's check that the workflow runs and the triage agent correctly routes between the two specialist agents.</p>
<div class="language-python highlight"><pre id="__code_7"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_7 > code"></button><code class="md-code__content"><span id="__span-7-1"><a id="__codelineno-7-1" name="__codelineno-7-1" href="#__codelineno-7-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">agents</span><span class="w"> </span><span class="kn">import</span> <span class="n">Runner</span>
</span><span id="__span-7-2"><a id="__codelineno-7-2" name="__codelineno-7-2" href="#__codelineno-7-2"></a>
</span><span id="__span-7-3"><a id="__codelineno-7-3" name="__codelineno-7-3" href="#__codelineno-7-3"></a><span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">main</span><span class="p">():</span>
</span><span id="__span-7-4"><a id="__codelineno-7-4" name="__codelineno-7-4" href="#__codelineno-7-4"></a>    <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">Runner</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">triage_agent</span><span class="p">,</span> <span class="s2">"What is the capital of France?"</span><span class="p">)</span>
</span><span id="__span-7-5"><a id="__codelineno-7-5" name="__codelineno-7-5" href="#__codelineno-7-5"></a>    <span class="nb">print</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">final_output</span><span class="p">)</span>
</span></code></pre></div>
<h2 id="add-a-guardrail">Add a guardrail</h2>
<p>You can define custom guardrails to run on the input or output.</p>
<div class="language-python highlight"><pre id="__code_8"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_8 > code"></button><code class="md-code__content" tabindex="0"><span id="__span-8-1"><a id="__codelineno-8-1" name="__codelineno-8-1" href="#__codelineno-8-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">agents</span><span class="w"> </span><span class="kn">import</span> <span class="n">GuardrailFunctionOutput</span><span class="p">,</span> <span class="n">Agent</span><span class="p">,</span> <span class="n">Runner</span>
</span><span id="__span-8-2"><a id="__codelineno-8-2" name="__codelineno-8-2" href="#__codelineno-8-2"></a><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic</span><span class="w"> </span><span class="kn">import</span> <span class="n">BaseModel</span>
</span><span id="__span-8-3"><a id="__codelineno-8-3" name="__codelineno-8-3" href="#__codelineno-8-3"></a>
</span><span id="__span-8-4"><a id="__codelineno-8-4" name="__codelineno-8-4" href="#__codelineno-8-4"></a><span class="k">class</span><span class="w"> </span><span class="nc">HomeworkOutput</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
</span><span id="__span-8-5"><a id="__codelineno-8-5" name="__codelineno-8-5" href="#__codelineno-8-5"></a>    <span class="n">is_homework</span><span class="p">:</span> <span class="nb">bool</span>
</span><span id="__span-8-6"><a id="__codelineno-8-6" name="__codelineno-8-6" href="#__codelineno-8-6"></a>    <span class="n">reasoning</span><span class="p">:</span> <span class="nb">str</span>
</span><span id="__span-8-7"><a id="__codelineno-8-7" name="__codelineno-8-7" href="#__codelineno-8-7"></a>
</span><span id="__span-8-8"><a id="__codelineno-8-8" name="__codelineno-8-8" href="#__codelineno-8-8"></a><span class="n">guardrail_agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span>
</span><span id="__span-8-9"><a id="__codelineno-8-9" name="__codelineno-8-9" href="#__codelineno-8-9"></a>    <span class="n">name</span><span class="o">=</span><span class="s2">"Guardrail check"</span><span class="p">,</span>
</span><span id="__span-8-10"><a id="__codelineno-8-10" name="__codelineno-8-10" href="#__codelineno-8-10"></a>    <span class="n">instructions</span><span class="o">=</span><span class="s2">"Check if the user is asking about homework."</span><span class="p">,</span>
</span><span id="__span-8-11"><a id="__codelineno-8-11" name="__codelineno-8-11" href="#__codelineno-8-11"></a>    <span class="n">output_type</span><span class="o">=</span><span class="n">HomeworkOutput</span><span class="p">,</span>
</span><span id="__span-8-12"><a id="__codelineno-8-12" name="__codelineno-8-12" href="#__codelineno-8-12"></a><span class="p">)</span>
</span><span id="__span-8-13"><a id="__codelineno-8-13" name="__codelineno-8-13" href="#__codelineno-8-13"></a>
</span><span id="__span-8-14"><a id="__codelineno-8-14" name="__codelineno-8-14" href="#__codelineno-8-14"></a><span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">homework_guardrail</span><span class="p">(</span><span class="n">ctx</span><span class="p">,</span> <span class="n">agent</span><span class="p">,</span> <span class="n">input_data</span><span class="p">):</span>
</span><span id="__span-8-15"><a id="__codelineno-8-15" name="__codelineno-8-15" href="#__codelineno-8-15"></a>    <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">Runner</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">guardrail_agent</span><span class="p">,</span> <span class="n">input_data</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="n">ctx</span><span class="o">.</span><span class="n">context</span><span class="p">)</span>
</span><span id="__span-8-16"><a id="__codelineno-8-16" name="__codelineno-8-16" href="#__codelineno-8-16"></a>    <span class="n">final_output</span> <span class="o">=</span> <span class="n">result</span><span class="o">.</span><span class="n">final_output_as</span><span class="p">(</span><span class="n">HomeworkOutput</span><span class="p">)</span>
</span><span id="__span-8-17"><a id="__codelineno-8-17" name="__codelineno-8-17" href="#__codelineno-8-17"></a>    <span class="k">return</span> <span class="n">GuardrailFunctionOutput</span><span class="p">(</span>
</span><span id="__span-8-18"><a id="__codelineno-8-18" name="__codelineno-8-18" href="#__codelineno-8-18"></a>        <span class="n">output_info</span><span class="o">=</span><span class="n">final_output</span><span class="p">,</span>
</span><span id="__span-8-19"><a id="__codelineno-8-19" name="__codelineno-8-19" href="#__codelineno-8-19"></a>        <span class="n">tripwire_triggered</span><span class="o">=</span><span class="ow">not</span> <span class="n">final_output</span><span class="o">.</span><span class="n">is_homework</span><span class="p">,</span>
</span><span id="__span-8-20"><a id="__codelineno-8-20" name="__codelineno-8-20" href="#__codelineno-8-20"></a>    <span class="p">)</span>
</span></code></pre></div>
<h2 id="put-it-all-together">Put it all together</h2>
<p>Let's put it all together and run the entire workflow, using handoffs and the input guardrail.</p>
<div class="language-python highlight"><pre id="__code_9"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_9 > code"></button><code class="md-code__content" tabindex="0"><span id="__span-9-1"><a id="__codelineno-9-1" name="__codelineno-9-1" href="#__codelineno-9-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">agents</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span><span class="p">,</span> <span class="n">InputGuardrail</span><span class="p">,</span> <span class="n">GuardrailFunctionOutput</span><span class="p">,</span> <span class="n">Runner</span>
</span><span id="__span-9-2"><a id="__codelineno-9-2" name="__codelineno-9-2" href="#__codelineno-9-2"></a><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic</span><span class="w"> </span><span class="kn">import</span> <span class="n">BaseModel</span>
</span><span id="__span-9-3"><a id="__codelineno-9-3" name="__codelineno-9-3" href="#__codelineno-9-3"></a><span class="kn">import</span><span class="w"> </span><span class="nn">asyncio</span>
</span><span id="__span-9-4"><a id="__codelineno-9-4" name="__codelineno-9-4" href="#__codelineno-9-4"></a>
</span><span id="__span-9-5"><a id="__codelineno-9-5" name="__codelineno-9-5" href="#__codelineno-9-5"></a><span class="k">class</span><span class="w"> </span><span class="nc">HomeworkOutput</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
</span><span id="__span-9-6"><a id="__codelineno-9-6" name="__codelineno-9-6" href="#__codelineno-9-6"></a>    <span class="n">is_homework</span><span class="p">:</span> <span class="nb">bool</span>
</span><span id="__span-9-7"><a id="__codelineno-9-7" name="__codelineno-9-7" href="#__codelineno-9-7"></a>    <span class="n">reasoning</span><span class="p">:</span> <span class="nb">str</span>
</span><span id="__span-9-8"><a id="__codelineno-9-8" name="__codelineno-9-8" href="#__codelineno-9-8"></a>
</span><span id="__span-9-9"><a id="__codelineno-9-9" name="__codelineno-9-9" href="#__codelineno-9-9"></a><span class="n">guardrail_agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span>
</span><span id="__span-9-10"><a id="__codelineno-9-10" name="__codelineno-9-10" href="#__codelineno-9-10"></a>    <span class="n">name</span><span class="o">=</span><span class="s2">"Guardrail check"</span><span class="p">,</span>
</span><span id="__span-9-11"><a id="__codelineno-9-11" name="__codelineno-9-11" href="#__codelineno-9-11"></a>    <span class="n">instructions</span><span class="o">=</span><span class="s2">"Check if the user is asking about homework."</span><span class="p">,</span>
</span><span id="__span-9-12"><a id="__codelineno-9-12" name="__codelineno-9-12" href="#__codelineno-9-12"></a>    <span class="n">output_type</span><span class="o">=</span><span class="n">HomeworkOutput</span><span class="p">,</span>
</span><span id="__span-9-13"><a id="__codelineno-9-13" name="__codelineno-9-13" href="#__codelineno-9-13"></a><span class="p">)</span>
</span><span id="__span-9-14"><a id="__codelineno-9-14" name="__codelineno-9-14" href="#__codelineno-9-14"></a>
</span><span id="__span-9-15"><a id="__codelineno-9-15" name="__codelineno-9-15" href="#__codelineno-9-15"></a><span class="n">math_tutor_agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span>
</span><span id="__span-9-16"><a id="__codelineno-9-16" name="__codelineno-9-16" href="#__codelineno-9-16"></a>    <span class="n">name</span><span class="o">=</span><span class="s2">"Math Tutor"</span><span class="p">,</span>
</span><span id="__span-9-17"><a id="__codelineno-9-17" name="__codelineno-9-17" href="#__codelineno-9-17"></a>    <span class="n">handoff_description</span><span class="o">=</span><span class="s2">"Specialist agent for math questions"</span><span class="p">,</span>
</span><span id="__span-9-18"><a id="__codelineno-9-18" name="__codelineno-9-18" href="#__codelineno-9-18"></a>    <span class="n">instructions</span><span class="o">=</span><span class="s2">"You provide help with math problems. Explain your reasoning at each step and include examples"</span><span class="p">,</span>
</span><span id="__span-9-19"><a id="__codelineno-9-19" name="__codelineno-9-19" href="#__codelineno-9-19"></a><span class="p">)</span>
</span><span id="__span-9-20"><a id="__codelineno-9-20" name="__codelineno-9-20" href="#__codelineno-9-20"></a>
</span><span id="__span-9-21"><a id="__codelineno-9-21" name="__codelineno-9-21" href="#__codelineno-9-21"></a><span class="n">history_tutor_agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span>
</span><span id="__span-9-22"><a id="__codelineno-9-22" name="__codelineno-9-22" href="#__codelineno-9-22"></a>    <span class="n">name</span><span class="o">=</span><span class="s2">"History Tutor"</span><span class="p">,</span>
</span><span id="__span-9-23"><a id="__codelineno-9-23" name="__codelineno-9-23" href="#__codelineno-9-23"></a>    <span class="n">handoff_description</span><span class="o">=</span><span class="s2">"Specialist agent for historical questions"</span><span class="p">,</span>
</span><span id="__span-9-24"><a id="__codelineno-9-24" name="__codelineno-9-24" href="#__codelineno-9-24"></a>    <span class="n">instructions</span><span class="o">=</span><span class="s2">"You provide assistance with historical queries. Explain important events and context clearly."</span><span class="p">,</span>
</span><span id="__span-9-25"><a id="__codelineno-9-25" name="__codelineno-9-25" href="#__codelineno-9-25"></a><span class="p">)</span>
</span><span id="__span-9-26"><a id="__codelineno-9-26" name="__codelineno-9-26" href="#__codelineno-9-26"></a>
</span><span id="__span-9-27"><a id="__codelineno-9-27" name="__codelineno-9-27" href="#__codelineno-9-27"></a>
</span><span id="__span-9-28"><a id="__codelineno-9-28" name="__codelineno-9-28" href="#__codelineno-9-28"></a><span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">homework_guardrail</span><span class="p">(</span><span class="n">ctx</span><span class="p">,</span> <span class="n">agent</span><span class="p">,</span> <span class="n">input_data</span><span class="p">):</span>
</span><span id="__span-9-29"><a id="__codelineno-9-29" name="__codelineno-9-29" href="#__codelineno-9-29"></a>    <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">Runner</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">guardrail_agent</span><span class="p">,</span> <span class="n">input_data</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="n">ctx</span><span class="o">.</span><span class="n">context</span><span class="p">)</span>
</span><span id="__span-9-30"><a id="__codelineno-9-30" name="__codelineno-9-30" href="#__codelineno-9-30"></a>    <span class="n">final_output</span> <span class="o">=</span> <span class="n">result</span><span class="o">.</span><span class="n">final_output_as</span><span class="p">(</span><span class="n">HomeworkOutput</span><span class="p">)</span>
</span><span id="__span-9-31"><a id="__codelineno-9-31" name="__codelineno-9-31" href="#__codelineno-9-31"></a>    <span class="k">return</span> <span class="n">GuardrailFunctionOutput</span><span class="p">(</span>
</span><span id="__span-9-32"><a id="__codelineno-9-32" name="__codelineno-9-32" href="#__codelineno-9-32"></a>        <span class="n">output_info</span><span class="o">=</span><span class="n">final_output</span><span class="p">,</span>
</span><span id="__span-9-33"><a id="__codelineno-9-33" name="__codelineno-9-33" href="#__codelineno-9-33"></a>        <span class="n">tripwire_triggered</span><span class="o">=</span><span class="ow">not</span> <span class="n">final_output</span><span class="o">.</span><span class="n">is_homework</span><span class="p">,</span>
</span><span id="__span-9-34"><a id="__codelineno-9-34" name="__codelineno-9-34" href="#__codelineno-9-34"></a>    <span class="p">)</span>
</span><span id="__span-9-35"><a id="__codelineno-9-35" name="__codelineno-9-35" href="#__codelineno-9-35"></a>
</span><span id="__span-9-36"><a id="__codelineno-9-36" name="__codelineno-9-36" href="#__codelineno-9-36"></a><span class="n">triage_agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span>
</span><span id="__span-9-37"><a id="__codelineno-9-37" name="__codelineno-9-37" href="#__codelineno-9-37"></a>    <span class="n">name</span><span class="o">=</span><span class="s2">"Triage Agent"</span><span class="p">,</span>
</span><span id="__span-9-38"><a id="__codelineno-9-38" name="__codelineno-9-38" href="#__codelineno-9-38"></a>    <span class="n">instructions</span><span class="o">=</span><span class="s2">"You determine which agent to use based on the user's homework question"</span><span class="p">,</span>
</span><span id="__span-9-39"><a id="__codelineno-9-39" name="__codelineno-9-39" href="#__codelineno-9-39"></a>    <span class="n">handoffs</span><span class="o">=</span><span class="p">[</span><span class="n">history_tutor_agent</span><span class="p">,</span> <span class="n">math_tutor_agent</span><span class="p">],</span>
</span><span id="__span-9-40"><a id="__codelineno-9-40" name="__codelineno-9-40" href="#__codelineno-9-40"></a>    <span class="n">input_guardrails</span><span class="o">=</span><span class="p">[</span>
</span><span id="__span-9-41"><a id="__codelineno-9-41" name="__codelineno-9-41" href="#__codelineno-9-41"></a>        <span class="n">InputGuardrail</span><span class="p">(</span><span class="n">guardrail_function</span><span class="o">=</span><span class="n">homework_guardrail</span><span class="p">),</span>
</span><span id="__span-9-42"><a id="__codelineno-9-42" name="__codelineno-9-42" href="#__codelineno-9-42"></a>    <span class="p">],</span>
</span><span id="__span-9-43"><a id="__codelineno-9-43" name="__codelineno-9-43" href="#__codelineno-9-43"></a><span class="p">)</span>
</span><span id="__span-9-44"><a id="__codelineno-9-44" name="__codelineno-9-44" href="#__codelineno-9-44"></a>
</span><span id="__span-9-45"><a id="__codelineno-9-45" name="__codelineno-9-45" href="#__codelineno-9-45"></a><span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">main</span><span class="p">():</span>
</span><span id="__span-9-46"><a id="__codelineno-9-46" name="__codelineno-9-46" href="#__codelineno-9-46"></a>    <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">Runner</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">triage_agent</span><span class="p">,</span> <span class="s2">"who was the first president of the united states?"</span><span class="p">)</span>
</span><span id="__span-9-47"><a id="__codelineno-9-47" name="__codelineno-9-47" href="#__codelineno-9-47"></a>    <span class="nb">print</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">final_output</span><span class="p">)</span>
</span><span id="__span-9-48"><a id="__codelineno-9-48" name="__codelineno-9-48" href="#__codelineno-9-48"></a>
</span><span id="__span-9-49"><a id="__codelineno-9-49" name="__codelineno-9-49" href="#__codelineno-9-49"></a>    <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">Runner</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">triage_agent</span><span class="p">,</span> <span class="s2">"what is life"</span><span class="p">)</span>
</span><span id="__span-9-50"><a id="__codelineno-9-50" name="__codelineno-9-50" href="#__codelineno-9-50"></a>    <span class="nb">print</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">final_output</span><span class="p">)</span>
</span><span id="__span-9-51"><a id="__codelineno-9-51" name="__codelineno-9-51" href="#__codelineno-9-51"></a>
</span><span id="__span-9-52"><a id="__codelineno-9-52" name="__codelineno-9-52" href="#__codelineno-9-52"></a><span class="k">if</span> <span class="vm">__name__</span> <span class="o">==</span> <span class="s2">"__main__"</span><span class="p">:</span>
</span><span id="__span-9-53"><a id="__codelineno-9-53" name="__codelineno-9-53" href="#__codelineno-9-53"></a>    <span class="n">asyncio</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">main</span><span class="p">())</span>
</span></code></pre></div>
<h2 id="view-your-traces">View your traces</h2>
<p>To review what happened during your agent run, navigate to the <a href="https://platform.openai.com/traces">Trace viewer in the OpenAI Dashboard</a> to view traces of your agent runs.</p>
<h2 id="next-steps">Next steps</h2>
<p>Learn how to build more complex agentic flows:</p>
<ul>
<li>Learn about how to configure <a href="../agents/">Agents</a>.</li>
<li>Learn about <a href="../running_agents/">running agents</a>.</li>
<li>Learn about <a href="../tools/">tools</a>, <a href="../guardrails/">guardrails</a> and <a href="../models/">models</a>.</li>
</ul>












                
              </article>
            </div>
          
          
<script>var target=document.getElementById(location.hash.slice(1));target&&target.name&&(target.checked=target.name.startsWith("__tabbed_"))</script>
        </div>
        
      </main>
      
        <footer class="md-footer">
  
  <div class="md-footer-meta md-typeset">
    <div class="md-footer-meta__inner md-grid">
      <div class="md-copyright">
  
  
</div>
      
    </div>
  </div>
</footer>
      
    </div>
    <div class="md-dialog" data-md-component="dialog">
      <div class="md-dialog__inner md-typeset"></div>
    </div>
    
    
    
      
      <script id="__config" type="application/json">{"base": "..", "features": ["content.code.copy", "content.code.select", "navigation.path", "navigation.sections", "navigation.expand", "content.code.annotate"], "search": "../assets/javascripts/workers/search.f8cc74c7.min.js", "tags": null, "translations": {"clipboard.copied": "Copied to clipboard", "clipboard.copy": "Copy to clipboard", "search.result.more.one": "1 more on this page", "search.result.more.other": "# more on this page", "search.result.none": "No matching documents", "search.result.one": "1 matching document", "search.result.other": "# matching documents", "search.result.placeholder": "Type to start searching", "search.result.term.missing": "Missing", "select.version": "Select version"}, "version": null}</script>
    
    
      <script src="../assets/javascripts/bundle.c8b220af.min.js"></script>
      
    
  
</body>

```
