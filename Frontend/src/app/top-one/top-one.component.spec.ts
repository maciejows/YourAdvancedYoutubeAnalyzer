import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TopOneComponent } from './top-one.component';

describe('TopOneComponent', () => {
  let component: TopOneComponent;
  let fixture: ComponentFixture<TopOneComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TopOneComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TopOneComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
