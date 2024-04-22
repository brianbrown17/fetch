import { NgModule } from '@angular/core';
import { AgmCoreModule } from '@agm/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    AppRoutingModule,
    AgmCoreModule.forRoot({
      apiKey: 'AIzaSyAK7y39CILuS-5jYUzhQmmwz24z8UaFFpQ'
    })
  ],
  providers: [],
  bootstrap: [AppComponent]
})

export class AppModule {}